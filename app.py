import sqlite3
import scapy.all as scapy
from tkinter.filedialog import askopenfilename

class Vendor:
    def __init__(self, vendor_tuple, mac_addr):
        self.Registry, self.Assignment, self.Organization, self.Address = vendor_tuple 
        self.mac_addr = mac_addr

    def __str__(self):
        return f"Mac Address - {self.mac_addr}, Registry - {self.Registry}, Assignment - {self.Assignment}, Organization - {self.Organization}, Address - {self.Address}"
    
    def __eq__(self, other):
        return self.Assignment == other.Assignment
    
    def __hash__(self):
        return int(self.Assignment, 16)

def get_vendors(mac_addr):
    '''Input - Mac Address
       Output - List of Vendor Objects for the given Mac Address
    '''
    con = sqlite3.connect("mac.db")
    cur = con.cursor()
    result = cur.execute("SELECT * FROM mac WHERE Assignment = ?", [format_mac(mac_addr)]).fetchall()
    vendors = []
    for i in result:
        vendors.append(Vendor(i, mac_addr))
    con.close()
    return vendors

def format_mac(mac_addr):
    t = mac_addr.split(sep = ":", maxsplit = 4)
    fmac_addr = "".join(t[:3])
    fmac_addr = fmac_addr.upper()
    return fmac_addr

print("Enter file(pcap) path : ")
file = askopenfilename()
print(file)
pckts = scapy.rdpcap(file)
vendor_set = set()
fake_addrs = set()
for pckt in pckts:
    try :
        mac_addr = pckt['Ethernet'].src
        vendors = get_vendors(mac_addr)
        for vendor in vendors:
            vendor_set.add(vendor)
        if not vendors:
            fake_addrs.add(mac_addr)
    except:
        continue

print("Real Mac Addresses with Vendors : ")
for vendor in vendor_set:
    print(vendor)

print("\nFake Mac Addresses : ")
for mac_addr in fake_addrs:
    print(mac_addr)