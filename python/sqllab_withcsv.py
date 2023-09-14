import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
cur = conn.cursor() # This manages the command that we want to send - cursor = invoke-command

# CREATE TABLE statement

# CREATE TABLE table_name (
#    column1 datatype constraint,
#    column2 datatype constraint,
#    column3 datatype constraint,
#   ....
#); 

print("Dropping table")
dropstring = "DROP TABLE Student"
#cur.execute(dropstring)

print("Creating table")
sqlstring = "CREATE TABLE Student ( StudentID int NOT NULL PRIMARY KEY, FirstName nvarchar(40) NOT NULL, Surname nvarchar(30) NULL, Course nvarchar(30) NULL, City nvarchar(15) NULL )"
#cur.execute(sqlstring)

"""
insertrows = ["INSERT INTO Student (StudentID, FirstName,Surname,Course,City) VALUES (1,'Andrew','Taylor','DevOps Apprenticeship','Selby')",
             "INSERT INTO Student (StudentID, FirstName,Surname,Course,City) VALUES (2,'Richard','Taylor','Networking Apprenticeship','York')",
             "INSERT INTO Student (StudentID, FirstName,Surname,Course,City) VALUES (3,'Michael','Risby','DevOps Apprenticeship','Leeds')",
             "INSERT INTO Student (StudentID, FirstName,Surname,Course,City) VALUES (4,'Ryan','Smith','Operations Apprenticeship','Hull')",
             "INSERT INTO Student (StudentID, FirstName,Surname,Course,City) VALUES (5,'James','Brown','Music Apprenticeship','London')"]
"""
print("Inserting rows")
#for record in insertrows:
    #cur.execute(record)
    #conn.commit()

print("Updating records")
sqlqueryvar = "UPDATE Student SET City = 'Doncaster' WHERE StudentID = 5"
#cur.execute(sqlqueryvar)
#conn.commit()

studentlist = []

StudentsFile = open("python/students.csv")
StudentsToAdd = StudentsFile.readlines()
StudentsFile.close()
print(StudentsToAdd)

for line in StudentsToAdd:
    student = line.split(",")
    print(student)
    studentlist.append(student)

print("Student list index 0")
print(studentlist[0][1])

for student in studentlist:
    sqlstring = "INSERT INTO Student (StudentID, FirstName,Surname,Course,City) VALUES (",studentlist[0][0]",",studentlist[0][1]",",studentlist[0][2]",",studentlist[0][3]",",studentlist[0][1]")"
    print(sqlstring)

#conn.commit()
conn.close()