import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="smartpill"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Define a function to add a new pill to the database
def add_pill(name, dosage, frequency):
    sql = "INSERT INTO pills (name, dosage, frequency) VALUES (%s, %s, %s)"
    val = (name, dosage, frequency)
    mycursor.execute(sql, val)
    mydb.commit()

# Define a function to retrieve all pills from the database
def get_all_pills():
    mycursor.execute("SELECT * FROM pills")
    result = mycursor.fetchall()
    return result

# Define a function to update the details of a pill in the database
def update_pill(id, name, dosage, frequency):
    sql = "UPDATE pills SET name = %s, dosage = %s, frequency = %s WHERE id = %s"
    val = (name, dosage, frequency, id)
    mycursor.execute(sql, val)
    mydb.commit()

# Define a function to delete a pill from the database
def delete_pill(id):
    sql = "DELETE FROM pills WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
