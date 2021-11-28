import sqlite3
import scapy.all as scapy

class Vendor:
    def __init__(self, vendor_tuple):
        self.Registry, self.Assignment, self.Organization, self.Address = vendor_tuple

    def __str__(self):
        return f"Registry - {self.Registry}, Assignment - {self.Assignment}, Organization - {self.Organization}, Address - {self.Address}"

def get_vendors(mac_addr):
    '''Input - Mac Address
       Output - List of Vendor Objects for the given Mac Address
    '''
    con = sqlite3.connect("mac.db")
    cur = con.cursor()
    result = cur.execute("SELECT * FROM mac WHERE Assignment = ?", [mac_addr]).fetchall()
    vendors = []
    for i in result:
        vendors.append(Vendor(i))
    con.close()
    return vendors

def format_mac(mac_addr):
    t = mac_addr.split(sep = ":", maxsplit = 4)
    fmac_addr = "".join(t[:3])
    fmac_addr = fmac_addr.upper()
    return fmac_addr

file = input("Enter file(pcap) path : ")
pckts = scapy.rdpcap(file)
for pckt in pckts:
    mac_addr = pckt['Ethernet'].src
    vendors = get_vendors(format_mac(mac_addr))
    for vendor in vendors:
        print(vendor)