import sqlite3

con=sqlite3.connect("test.db")
cur=con.cursor()

#list all the tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cur.fetchall()
print("Tables in the database:", tables)

#query from the first table
if tables:
    first_table=tables[0][0]
    cur.execute(f"SELECT * FROM {first_table};")
    rows=cur.fetchall()
    print(f"Data in table {first_table}:")
    for row in rows:
        print(row)

con.close()