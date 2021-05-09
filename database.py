import sqlite3

conn = sqlite3.connect('covid.db')
c = conn.cursor()

# c.execute("""CREATE TABLE hospital_bed (
#         hospital_id KEY,
#         hospital_name text,
#         total_beds integer,
#         vacant_beds integer,
#         address text,
#         phone_no integer
#         )""")


# c.execute("""Insert into hospital_bed values(1,'mgm',100,15,'kamothe',80700876)""")
#c.execute("""Insert into hospital_bed values(2,'apollo',100,25,'belapur',80700852)""")

c.execute("""SELECT * FROM hospital_bed""")
print(c.fetchall())


conn.commit()
conn.close()

