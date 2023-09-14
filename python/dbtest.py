import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
cur = conn.cursor() # This manages the command that we want to send - cursor = invoke-command
result = cur.execute('SELECT * FROM company').fetchall()

for row in result:
    print(row)

# SQL query syntax

# SELECT * FROM company - SELECT ALL FROM company table
# SELECT company_name, country, post_code FROM company
# SELECT <colum names> FROM table 

# The WHERE clause

# SELECT <colum names> FROM table WHERE <filter>

sqlqueryvar = 'SELECT * FROM company'

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)

sqlqueryvar = 'SELECT company_name, county, post_code FROM company WHERE company_no > 2000'

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)

sqlqueryvar = 'SELECT company_name, county, post_code FROM company WHERE company_no BETWEEN 1001 AND 3001'

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)

sqlqueryvar = "SELECT company_name, county, post_code FROM company WHERE company_name LIKE '%Inc'"

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)

# Where in clause
sqlqueryvar = "SELECT company_name, county, post_code FROM company WHERE county IN ('London','Devon')"

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)

# ORder by descending
sqlqueryvar = 'SELECT * FROM company ORDER BY company_no DESC'

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)


# Group by clause -  SELECT <col_name>,<aggregates> FROM <tablename> GROUP BY <col_name>

sqlqueryvar = 'SELECT emp_no, sum(order_value), count(emp_no) AS Total_Sales FROM sale GROUP BY emp_no'

result = cur.execute(sqlqueryvar).fetchall()

for row in result:
    print(row)

conn.close()