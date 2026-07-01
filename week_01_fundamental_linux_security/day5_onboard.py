# Identity Database Audit
import sys

def audit_onboarding_list(user_list):
    print("=== Identity Database Sweep ===")
    existing_users = ["admin", "root", "siya_mathew"]

    for user in user_list:
        if user in existing_users:
            print(f"[-] MITRE T1078 Warning: '{user}' already holds a valid account. Skipping.")
        else:
            print(f"[+] Provisioning Allowed: Creating secure identity node for '{user}'.")

# Test system dataset
new_hires = ["siya_mathew", "cloud_bot", "security_intern"]
audit_onboarding_list(new_hires)
