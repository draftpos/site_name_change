# Copyright (c) 2026, munyaradzi chirove and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import os
import subprocess
import json

class SiteChange(Document):
    def before_save(self):
        job = frappe.enqueue(
            run_site_change_bg,
            old_site=self.old_site_name,
            new_site=self.new_site_name,
            db_password=self.db_password,
            docname=self.name,
            queue="long",
            timeout=20000
        )
        frappe.msgprint(f"🚀 Site change queued in background. Job ID: {job.id}")

@frappe.whitelist()
def run_site_change_bg(old_site, new_site, db_password, docname):
    """
    Background job that actually performs the site change
    """
    logger = frappe.logger("site_change")

    try:
        logger.info(f"Starting site change: {old_site} → {new_site}")

        # load the doc
        doc = frappe.get_doc("Site Change", docname)

        # 1️⃣ Save old site config
        config = get_site_config_direct(old_site)
        doc.old_site_configs = json.dumps(config, indent=4)
        doc.db_update()
        logger.info("Old site config captured")

        # 2️⃣ Create new site
        create_new_site_no_prompt(
            new_site=new_site,
            admin_password="admin",
            mariadb_root=db_password
        )
        logger.info("New site created")

        # 3️⃣ Switch site config
        switch_site_config(old_site, new_site)
        logger.info("Site config switched")

        frappe.db.commit()
        logger.info(f"✅ Site change completed: {old_site} → {new_site}")

    except Exception:
        frappe.log_error(
            frappe.get_traceback(),
            f"Site Change Failed: {old_site} → {new_site}"
        )
        raise frappe.msgprint(f"Site Change Before Save Hook Triggered for {old_site} to {new_site}")

def create_new_site_no_prompt(new_site, admin_password="admin", mariadb_root=None):
    if not mariadb_root:
        mariadb_root = (
            frappe.conf.get("mariadb_root_password")
            or frappe.conf.get("db_root_password")
        )

    if not mariadb_root:
        frappe.log_error(
            title="create_new_site_no_prompt – Missing DB root password",
            message=f"Site: {new_site}\nMariaDB root password not found in frappe config"
        )
        frappe.throw("MariaDB root password not found in frappe config")

    cmd = [
        "bench",
        "new-site",
        new_site,
        "--admin-password", str(admin_password),
        "--mariadb-root-password", str(mariadb_root),
    ]

    # UI-visible log (before execution)
    frappe.log_error(
        title="create_new_site_no_prompt – Starting",
        message=f"Running command:\n{' '.join(cmd)}"
    )

    try:
        subprocess.run(cmd, check=True)
    except Exception:
        frappe.log_error(
            title="create_new_site_no_prompt – Failed",
            message=frappe.get_traceback()
        )
        raise

    # UI-visible success log
    frappe.log_error(
        title="create_new_site_no_prompt – Success",
        message=f"New site created successfully: {new_site}"
    )

    frappe.msgprint(f"✅ New site '{new_site}' created!")


def list_apps_via_bench(site_name):
    apps = []

    command = [
        "bench",
        "--site", site_name,
        "list-apps"
    ]

    # Spawn the process
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True  # ensures strings, not bytes
    )

    # Read output line by line
    for line in process.stdout:
        apps.append(line.strip())

    process.wait()

    if process.returncode == 0:
        print(f"\n✅ Done listing apps for {site_name}")
        return apps
    else:
        print(f"\n❌ Bench execute failed with code {process.returncode}")
        return []

def switch_site_config(old_site, new_site):
    try:
        bench_path = frappe.utils.get_bench_path()
        old_config = os.path.join(bench_path, "sites", old_site, "site_config.json")
        new_config = os.path.join(bench_path, "sites", new_site, "site_config.json")

        # Remove new site config
        subprocess.run(["rm", "-f", new_config], check=True)

        # Copy old config
        subprocess.run(["cp", old_config, new_config], check=True)

        # ✅ SUCCESS LOG (shows in UI)
        frappe.log_error(
            title="Site Config Switch SUCCESS",
            message=f"""
            Old Site: {old_site}
            New Site: {new_site}

            Old Config:
            {old_config}

            New Config:
            {new_config}
            """
        )

    except Exception as e:
        # ❌ ERROR LOG (also UI)
        frappe.log_error(
            title="Site Config Switch FAILED",
            message=frappe.get_traceback()
        )
        raise

def get_site_config_direct(site_name):
    """
    Reads site_config.json directly for the given site.
    """
    bench_path = frappe.utils.get_bench_path()
    site_path = os.path.join(
        bench_path,
        "sites",
        site_name,
        "site_config.json"
    )

    if not os.path.exists(site_path):
        frappe.log_error(
            title="get_site_config_direct – Missing file",
            message=f"site_config.json not found\nSite: {site_name}\nPath: {site_path}"
        )
        frappe.throw(f"site_config.json not found for site: {site_name}")

    try:
        with open(site_path, "r") as f:
            config = json.load(f)

    except Exception:
        frappe.log_error(
            title="get_site_config_direct – Read failed",
            message=frappe.get_traceback()
        )
        frappe.throw("Failed to read site_config.json (see Error Log)")

    # Optional success log (safe, no mutation)
    frappe.log_error(
        title="get_site_config_direct – Success",
        message=f"Read site_config.json successfully for site: {site_name}"
    )

    return config

