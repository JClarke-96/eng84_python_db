# Establish connection between Python and SQL
import pyodbc
from nw_products import Products

# Establish connection using PYODBC
server = "__"
database = "__"
username = "__"
password = "__"
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Check if connection is validated and cursor object created
cursor = docker_Northwind.cursor()
print(cursor.execute("SELECT @@version;"))

# Connect to DB and fetch data from Customers
products_table = cursor.execute("SELECT * FROM Products").fetchall()
