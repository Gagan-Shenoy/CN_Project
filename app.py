import sqlite3

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

print("Enter a Mac address : ")
vendors = get_vendors(input())
for vendor in vendors:
    print(vendor)