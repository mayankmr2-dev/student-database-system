import pyodbc  # For python3 MSSQL

cnxn = pyodbc.connect("Driver={SQL Server};"  # For Connection
                      "Server=RAPTAR\SQLEXPRESS;"
                      "Database=Emprecords;"
                      "Trusted_Connection=yes"
                      "Uid=mayan;"
                      "Pwd=pass@123;")
cursor = cnxn.cursor()  # Cursor Establishment
cursor.execute('select * from Emptable')  # Execute Query
# cursor.fetchall()
# print(cursor.fetchone())  # fetch the first row only

# cnxn.close()


for row in cursor.fetchall():
    print(row.Empid, row.Empname)


# cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"  # For Connection
#                       "Server=49.50.100.159,5263;"
#                       "Database=practicemk;"
#                       #   "Trusted_Connection=yes"
#                       "Uid=mayankmr2;"
#                       "Pwd=Mayan@1198;")
# cursor = cnxn.cursor()  # Cursor Establishment
# cursor.execute('select * from student')  # Execute Query

# for row in cursor:
#     print('row = %r' % (row,))
