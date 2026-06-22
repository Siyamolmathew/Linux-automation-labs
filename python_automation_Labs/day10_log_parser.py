import os

print("=============================================")
print("    DAY  10: AUTOMATED SECURITY LOG PARSER   ")
print("=============================================")

log_path ="../system_audit.log"
error_count = 0

print(f"[*] Intiating scan on information log: {log_path}\n")

# 1. Defensive check: Ensure the file exists before reading
if os.path.exists(log_path):
    # 2. Opening and read the file line-by-line streaming memory efficiently
    with open(log_path,"r")as file:
        for line_num, line in enumerate(file, 1):
            # Clean up trailing whitespace/newlines
            clean_line = line.strip()

            # 3. Core filter: Isolate critical system threats
            if "ERROR" in clean_line.upper() or "UNAUTHORIZED" in clean_line.upper():
                error_count += 1
                print(f"[ALERT] line {line_num}: {clean_line}")
    print(f"\n Log analysis complete.")
    print(f" -> Total critical security events flagged: {error_count}")

else:
    print(f"Error: Target log file at '{log_path}' could not be located.")

print("\n===============================================================")
