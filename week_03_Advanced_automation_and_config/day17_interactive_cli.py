import sys
import re

def display_menu():
    print("\n==============================================")
    print("      WISE NETWORK OPERATIONS ENGINE v3.0     ")
    print("==============================================")
    print("1. Audit Local System Platform Info")
    print("2. Test Core Gateway Connectivity (Mock Ping)")
    print("3. Exit Terminal Session")
    print("==============================================")

def validate_ip(ip_str):
    """Uses a regular expression to verify if an input string matches a valid IPv4 structure."""
    ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(ipv4_pattern, ip_str) is not None

def start_interactive_engine():
    while True:
        display_menu()
        choice = input("[?] Select an operational track (1-3): ").strip()

        if choice == "1":
            print("\n[*] Fetching live resource context metrics...")
            print(f"[+] Active System Platform Target: {sys.platform}")
            print("[+] Status: Operational constraints are completely green.")
            
        elif choice == "2":
            target_ip = input("[?] Enter target node IP Address to ping: ").strip()
            # Apply dynamic regex validation check
            if validate_ip(target_ip):
                print(f"\n[*] ICMP Echo Stream initiated -> Transmitting packets to {target_ip}...")
                print(f"[+] 64 bytes from {target_ip}: icmp_seq=1 ttl=64 time=4.12ms")
                print(f"[+] Connection to {target_ip} verified successfully.")
            else:
                print("\n[🚨 ERROR] Input validation failed. That is not a valid IPv4 address pattern!")

        elif choice == "3":
            print("\n[+] Closing automation channel. Secure logout initiated. Goodbye!")
            sys.exit(0)
            
        else:
            print("\n[🚨 ERROR] Invalid selection. Please choose an options flag between 1 and 3.")

if __name__ == "__main__":
    try:
        start_interactive_engine()
    except KeyboardInterrupt:
        print("\n\n[-] Session terminated abruptly via exit signal sequence.")
        sys.exit(1)
