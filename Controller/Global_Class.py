import pyodbc
class Global:
    conn = pyodbc.connect('Driver={SQL Server};''Server=USER\SQLEXPRESS;''Database=FYP;''Trusted_Connection=yes;')
    cursor=conn.cursor()