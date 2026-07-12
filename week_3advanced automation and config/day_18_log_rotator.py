import os
import sys
import shutil
from datetime import datetime

def simulate_log_rotation(log_filename="production_traffic.log", max_size_bytes=1024):
    """Monitors log constraints and automatically rotates logs exceeding threshold sizes."""
    print("[*] Launching automated infrastructure log ratation audit...")
    print("==================================================================")

    # 1. Check if the target log file even exists; generate it if missing
    if not os.path.exists(log_filename):
        print("[-] Log target '{log_filename}' not found. Generating fresh mock stream context...")
        with open(log_filename, "w", encoding="utf-8") as file:
            file.write("INITIALIZATION BLOCK - Network traffic log stream open.\n" +
                       "Data entry stream standard line packet transaction metric logs.\n" * 25)

    # 2. Inspect current log volume metrics
    current_size = os.path.getsize(log_filename)
    print(f"[+] Active file: '{log_filename}' | Current Size: {current_size} bytes | Max Allowed: {max_size_bytes} bytes")

    # 3. Rotate logic threshold verification
    if current_size >= max_size_bytes:
        print("[Alert] Max log size constraint breached: Initiating rotation sequences...")

        # Generate timestamp suffix for backup archive file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = f"{log_filename}.{timestamp}.bak"
        try:
           # Safety clone current log data into the backup file string
           shutil.copyfile(log_filename, archive_name)
           print(f"[+] Log successfully archived to safety point: {archive_name}")

           # Truncare/wipe the active operational file back to empty to optimize storage blocks
           with open(log_filename, "w", encoding="utf-8")as active_file:
               active_file.write(f"--- LOG ROTATED AT {datetime.now().isoformat()} ---\n")

           print("[+] Active operational log file completely cleared and reset.")
           print("[+] Disk space optimized sucessfully. System state: GREEN.")
        except IOError as io_error:
           print(f"[-] Log status within normal operational boundaries. No rotation required.")
           sys.exist(1)
    else:
        print("[+] Log status within normal operational boundaries. No rotation required.")

if __name__ == "__main__":
    simulate_log_rotation()

