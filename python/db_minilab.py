import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
cur = conn.cursor() # This manages the command that we want to send - cursor = invoke-command

sqlquery = "SELECT first_name, last_name, salary, notes FROM salesperson WHERE salary BETWEEN 11.0000 AND 13.0000"
result = cur.execute(sqlquery).fetchall()

for row in result:
    print(row)

sqlquery = "SELECT contact_name, job_title, notes FROM contact WHERE job_title LIKE '%officer'"
result = cur.execute(sqlquery).fetchall()

for row in result:
    print(row)

sqlquery = "SELECT dept_name, manager FROM dept WHERE sales_target < 20.0000"
result = cur.execute(sqlquery).fetchall()

for row in result:
    print(row)

sqlquery = "SELECT first_name, last_name FROM salesperson WHERE dept_no IN (1,3)"
result = cur.execute(sqlquery).fetchall()

for row in result:
    print(row)

sqlquery = "SELECT order_no, company_no FROM sale WHERE contact_code = 'MM'"
result = cur.execute(sqlquery).fetchall()

for row in result:
    print(row)

conn.close()