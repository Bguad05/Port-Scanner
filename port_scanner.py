import socket 
import csv 
from datetime import datetime

PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    443: "HTTPS",
    3306: "MySQL",
}

def scan_port(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    try:
        s.connect((target_ip, port))
        s.close()
        return True 
    except:
        return False
    
def main():
    target_ip = input("Enter target IP address: ")
    results = []
    
    print(f"\n Beginning scan on {target_ip} at {datetime.now()}\n")
    
    for port, service in PORTS.items():
        if scan_port(target_ip, port):
            print(f"[OPEN] port {port} ({service})")
            results.append((port, service, "OPEN"))
        else:
            results.append((port, service, "CLOSED"))
            
        save = input("\n Do you want to save the results to a CSV file? (y/n): ").lower()
        
        if save == "y":
            with open("scan_results.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Port", "Service", "Status"])
                writer.writerows(results)
            print("Results saved to scan_results.csv")
            
if __name__== "__main__":
    main()