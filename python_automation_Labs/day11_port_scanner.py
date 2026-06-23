import socket 
import sys

print("==========================================")
print("   Day 11: NETWORK INFRASTRUCTURE AUDIT   ")
print("==========================================")

# 1. Target Configuration
# We will use a safe public DNS server (Google's Public DNS) to test connectivity
TARGET_HOST ="8.8.8.8" 
TARGET_PORT = 53 # Port 53 is dedicated to DNS  services

print(f"[*] Probing network target: {TARGET_HOST} on port{TARGET_PORT}..")

try:
   # 2. Initialize the Network Socket
   # AF_INET specifies IPv4 routing: SOCK_STREAM specifies TCP protocol connection
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as network_socket:

      # 3. Set a safety timeout limit (in seconda)
      network_socket.settimeout(2.0)
      # 4. Attempt the connection
      result_code = network_socket.connct_ex((TARGET_HOST, TARGET_PORT))
      # 5. Evalute the connection results
      if result_code == 0:
          print(f"[ALERT] Port {TARGET_PORT}  is OPEN and actively listening on {TARGET_HOST}!")
      else:
          print(f"Port {TARGET_PORT} is closed/filtered. (System Error Code: {result_code})")

except socket.gaierror:
    print("Network Error: Could not resolve the target hostname.")
except socket.timeout:
    print(" Network Error: Connection attempt timed out before matching host.")
except Exception as error:
    print(f" System Exception encountered: {error}")

print("\n==================================================")

