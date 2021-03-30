import pyodbc


class Products:
    def __init__(self):
        server = "__"
        database = "__"
        username = "__"
        password = "__"
        docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = docker_Northwind.cursor()

    def fetch_unitprice(self):
        pass

    def create_table(self):
        pass

    def retrieve_all_data_from_customers(self):
        row = cursor.execute("SELECT * FROM Customers")
        while True:
            record = row.fetchone()
            if record is None:
                break
            print(record.unitprice)
