# Establish connection between Python and SQL
import pyodbc

# Establish connection using PYODBC
server = "18.135.103.95"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Check if connection is validated and cursor object created
cursor = docker_Northwind.cursor()
print(cursor.execute("SELECT @@version;"))

# Fetch data from Northwind DB
row = cursor.fetchone()
print(row)

# Connect to DB and fetch data from Customers
customer_rows = cursor.execute("SELECT * FROM Customers").fetchall()
print(customer_rows)

# Iterate through Product table and print UnitPrice
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
for records in product_rows:
    print(records.UnitPrice)

row = cursor.execute("SELECT * FROM Products")
while True:
    record = row.fetchone()
    if record is None:
        break
    print(record.UnitPrice)
