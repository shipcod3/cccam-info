import sys
import telnetlib

def usage():
    print("""
    cccaminfo - by Jay Turla @shipcod3

    *********
    Usage:
    *********
    python cccaminfo.py <host>
    example -> cccaminfo.py localhost
    """)

"""
    Supported Commands:
    - info
    - activeclients
    - clients
    - servers
    - shares
    - providers
    - entitlements
"""

def main(argv):
    if len(argv) < 2:
        return usage()

    host = sys.argv[1]
    
    commands = [
        ("info", "Getting information on the receiver"),
        ("activeclients", "Active clients"),
        ("clients", "Clients"),
        ("servers", "Servers"),
        ("shares", "Shares"),
        ("providers", "Providers"),
        ("entitlements", "Entitlements")
    ]

    for command, description in commands:
        try:
            tn = telnetlib.Telnet(host, 16000)
            tn.read_until(b"Welcome to the CCcam information client.")
            print(f"[+] {description}\n")
            tn.write(command.encode() + b"\r")
            print(tn.read_all().decode())
        except Exception as e:
            print(f"[-] Error executing {command}: {e}")

if __name__ == "__main__":
    main(sys.argv)
