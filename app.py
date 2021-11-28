from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename
from mac import *

def open_file():
    filetypes = [('Pcap', '*.pcap')]
    file = askopenfilename(title = 'Open a file', filetypes = filetypes)
    vendor_set, fake_addrs = sort_mac_vendors(file)
    mac = Label(ws, text = 'Real Mac addresses')
    mac.grid(row = 5, column = 0, padx = 10)
    vendor_list = []
    for i in vendor_set:
        vendor_list.append(i.to_list())
    widths = [30, 10, 10, 50, 80]
    for i in range(len(vendor_list)):
        for j in range(5):
            e = Entry(ws, width = widths[j], font = ('Arial', 8,'bold'))
            e.grid(row = 6 + i, column = j)
            e.insert(END, vendor_list[i][j])
    fmac = Label(ws, text = 'Fake Mac addresses')
    fmac.grid(row = 7 + len(vendor_list), column = 0, padx = 10)
    fakeaddr_list = list(fake_addrs)
    for i in range(len(fakeaddr_list)):
        e = Entry(ws, width = 30, font = ('Arial', 8,'bold'))
        e.grid(row = 8 + len(vendor_list) + i, column = 0)
        e.insert(END, fakeaddr_list[i])

ws = Tk()
ws.title('MAC address analyser')
ws.geometry('1500x750')     
file = Label(ws, text = 'Upload Pcap file ')
file.grid(row = 0, column = 0, padx = 20)
filebtn = Button(ws, text = 'Choose File', command = open_file) 
filebtn.grid(row = 1, column = 0, padx = 20)
ws.mainloop()
