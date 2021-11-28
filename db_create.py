import csv
import sqlite3

con = sqlite3.connect("mac.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS mac")
cur.execute("CREATE TABLE mac (Registry text, Assignment text, Organization text, Address text);")
with open("oui_csv.csv", encoding="cp437") as f:
    reader = csv.DictReader(f)
    #field_names = reader.fieldnames 
    for row in reader:
        cur.execute("INSERT INTO mac VALUES (?, ?, ?, ?)", list(row.values()))
con.commit()
con.close()