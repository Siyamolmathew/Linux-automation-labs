import socket
import sys

print("=================================================")
print("      DAY 12 & 13: NETWORK BOUNDARY MAPPER       ")
print("=================================================\n")

try:
   # ------------------------------------------
   # PHASE 1: LOCAL NETWORK INTERFACE DISCOVERY
   #-------------------------------------------
   print("[*] Phase 1: Querying Local Network Inferfaces..")
   # Fetch local hostname and map it to the private network IP address
   local_hostname = socket.gethostname()
   internal_ip = socket.gethostname(local_hostname)

   print(f"  [+] System Hostname: {local_hostname}")
   print(f"  [+] Internet ip: {internal_ip}\n")

   #-------------------------------------------
   # PHASE 2: REMOTE COMPLIANCE PORT EDGE PROBE
   #-------------------------------------------
   # Target a stable public backbone server (Google Public DNS)
   TARGET_HOST = "8.8.8.8"
   CRITICAL_PORTS = [22, 53, 80, 443] #Array matrix of target ports

   print(f"[*] Phase 2: Evaluating External Edge Connectivity on {TARGET_HOST}...")
   print("------------------------------------------------------------------")

   #Loop through each critical port in our defind sequence
   for port in CRITICAL_PORTS:
       # Spawn an independant IPv4 (AF_INET) TCP (SOCK_STREAM) socket session
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe_socket:
           # Set a 1.5-second timeout to prevent the automation from hanging
           probe_socket.settimeout(1.5)

           # Execute connection attempt and capture numeric error return code
           status_code = probe_socket.connect_ex((TARGET_HOST, port))

           # Evalute the status code (0 means absolute connectivity success)
           if status_code == 0:
               print(f"[ALERT] Port {port:<3} -> OPEN | Traffic route accessible.")
           else:
               print(f" Port {port:<3} -> CLOSED | Protected/Filtered (Code: {status_code}) ")

   print("\n Diagnosis automation suite finished clean execution.")

except socket.gaierror:
    print("Critical Error: Network infrastructure hostname resolution failed.")
except Exception as unexpected_error:
    print(f"Fatal System Exception: {unexpected_error}")

print("===============================================")
   

