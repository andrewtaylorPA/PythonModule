import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
cur = conn.cursor() # This manages the command that we want to send - cursor = invoke-command


# SQL Insert statement
# INSERT into <tablename> (colname1, colname2) VALUES (val1, val2)

sqlquery = "INSERT INTO dept (dept_no,dept_name,manager,sales_target) VALUES (6,'IT','Andrew Taylor','50.0000')"

#cur.execute(sqlquery)
#conn.commit() # commit the insert back to the db

sqlqueryvar = 'SELECT * FROM dept'

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)

#Update statement

# UPDATE <tablename> SET <calname> = <value> , <calnam2> = <value2> where <filter>
# Filter is <col_name> <test char> <value>
#
sqlqueryvar = 'UPDATE dept SET sales_target = 55.0000 WHERE dept_no = 6'
cur.execute(sqlqueryvar)
conn.commit()

conn.close()
