import sys
import telnetlib

def usage():
    print """
    ccaminfo - by Jay Turla @shipcod3
    *********
    Usage:
    *********
    python ccaminfo.py <host> <command>
    example -> ccaminfo.py localhost clients

    *********
    Commands:
    *********
    - info
    - activeclients
    - clients
    - servers
    - shares
    - providers
    - entitlements
    """

def main(argv):
    if len(argv) < 3:
        return usage()

    host = sys.argv[1]
    command = sys.argv[2]
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    tn.write(command+"\r")
    print tn.read_all()

if __name__ == "__main__":
    main(sys.argv)
