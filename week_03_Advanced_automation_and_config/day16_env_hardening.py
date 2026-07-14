import os
import sys

def bootstrap_secure_configuration():
    """Validates and processes sensitive infrastructure parameters via decoupled environment bindings."""
    print("[*] Initializing Secure Infrastructure Bootstrapper...")
    print("=========================================================")

    # 1. Look for variables inside the environment context
    app_environment = os.environ.get("APP_ENV", "Development")  # Defaults safely to Development
    db_user = os.environ.get("DB_USER")
    api_token = os.environ.get("NET_API_TOKEN")

    print(f"[+] Active Operational Mode: {app_environment}")

    # 2. Strict validation rule: Critical secrets MUST exist if running in Production mode
    if app_environment.lower() == "production":
        if not db_user or not api_token:
            print("[🚨 CRITICAL ERROR] Production safety threshold breached!")
            print("[-] Decoupled environment secrets (DB_USER/NET_API_TOKEN) are missing.")
            print("[*] Terminating execution to protect company infrastructure assets.")
            sys.exit(1)

    # 3. Process data cleanly using fallbacks for testing
    resolved_user = db_user if db_user else "default_lab_user"
    
    # Securely mask sensitive tokens so they don't leak into logs or screens
    masked_token = f"************{api_token[-4:]}" if api_token else "NOT_SET_SECURELY"

    print("\n--- RESOLVED CONFIGURATION MATRIX ---")
    print(f"👤 Target Infrastructure User : {resolved_user}")
    print(f"🔑 Network API Access Token   : {masked_token}")
    print("-------------------------------------\n")
    print("[+] Bootstrap check complete. Configuration profile is stable.")

if __name__ == "__main__":
    bootstrap_secure_configuration()
