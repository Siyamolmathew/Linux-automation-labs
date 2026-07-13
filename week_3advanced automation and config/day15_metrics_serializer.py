import json
import os
import sys
import platform
import getpass
from datetime import datetime

def capture_system_telemetry():
    """Gathers raw system environment parameters and groups them into an explicit schema."""
    print("[*] Initiating Live Resource Target Audit...")
    try:
        # Cross-platform secure fallback configuration to find the active username
        try:
            username = getpass.getuser()
        except Exception:
            username = os.environ.get("USER") or os.environ.get("USERNAME") or "unknown"

        telemetry_payload = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "host_environment": {
                "operating_system": platform.system(),
                "kernel_release": platform.release(),
                "architecture": platform.machine()
            },
            "filesystem_boundary": {
                "working_directory": os.getcwd(),
                "user_context": username
            },
            "system_load_status": {
                "cpu_count": os.cpu_count() or 1,
                "process_id": os.getpid()
            }
        }
        return telemetry_payload
    except Exception as error:
        print(f"[-] Critical failure extracting hardware constraints: {error}")
        sys.exit(1)

def serialize_to_disk(payload, filename="system_metrics.json"):
    """Encodes standard Python dictionary maps into strict, validated JSON files on disk."""
    print(f"[*] Packaging metadata schema into target structural output: {filename}")
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(payload, json_file, indent=4, sort_keys=True)
            
        print(f"[+] Output File successfully compiled. Storage point locked: {os.path.abspath(filename)}")
        
        print("\n=== VERIFIED STRUCTURAL TELEMETRY PAYLOAD ===")
        print(json.dumps(payload, indent=2))
        print("==============================================\n")
    except IOError as write_error:
        print(f"[-] Core File I/O transaction interrupted: {write_error}")
        sys.exit(1)

if __name__ == "__main__":
    metrics = capture_system_telemetry()
    serialize_to_disk(metrics)
