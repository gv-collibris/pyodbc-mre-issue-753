import pyodbc

def test_function():
    server = "server"#TODO: change this
    database = "database"#TODO: change this
    connection_string = (
        'Driver={ODBC Driver 17 for SQL Server};'
        f'Server={server};Database={database}')
    connection = pyodbc.connect(connection_string)
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1890 * 1.0 / 100")
        print(cursor.fetchall())
