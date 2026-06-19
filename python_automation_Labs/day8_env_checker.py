import os
import sys

print("========================================")
print("  Day 8: SYSTEM ENVIRONMENT AUTOMATION  ")
print("========================================")

# 1.Fetching  current user and directory information
current_user = os.getlogin()
current_dir = os.getcwd()

print(f"[+] Current System User:{current_user}")
print(f"[+] Active Execution Path: {current_dir}\n")

# 2.Inspecting the Python Runtime Environment'
print("[+] Python ExecutableLocation:")
print(f"   -> {sys.executable}")
print(f"[+]Script Arguments Passed: {sys.argv}\n")

# 3. Checking for a specific Environment Variable
# (We will check if 'PATH' exists, which handles system command routes)
if "PATH" in os.environ:
    print(" Success: System 'PATH' environment variable is accessible.")
else:
    print(" Error: Environment variable isolated.")

print("\n===========================================")
