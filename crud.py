import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database = 'flights',
        auth_plugin='mysql_native_password')
    
    mycursor = conn.cursor()
    print('Connection Established')
except mysql.connector.Error as e:
    print(f'Connection Error: {e}')

"""
# Create a Database on the DB server
# Writing SQL query
try:
    mycursor.execute("CREATE DATABASE flights")
    conn.commit()
    print('Database "flights" created successfully')

except mysql.connector.Error as create_db_error:
    print(f"Error creating database: {create_db_error}")

except mysql.connector.Error as connect_error:
    print(f"Connection Error: {connect_error}")

"""

# create a table
# airport -> airport_id | code | name | city

#try:
#    mycursor.execute("""
#    CREATE TABLE airport(
#                    airport_id INTEGER PRIMARY KEY,
#                    code VARCHAR(10) NOT NULL,
#                    city VARCHAR(50) NOT NULL,
#                    name VARCHAR(50) NOT NULL 
#                        )
#    """)
#    conn.commit()

#except mysql.connector.Error as e:
#    print(f"Error creating table: {e}")

# Insert data into the table

#mycursor.execute("""
#INSERT INTO airport (airport_id, code, city, name)
#                 VALUES
#                 (1, 'DEL', 'New Delhi', 'IGIA'),
#                 (2, 'CCU', 'Kolkata', 'NSCA'),
#                 (3, 'BOM', 'Mumbai', 'CSMA')
#""")

#conn.commit()


# Search/ Retrive  operation
mycursor.execute(""" SELECT * from flights.airport """)

# featching result
data = mycursor.fetchall()
print(data)

#########################################
# change the city code (BOM) to MUM
mycursor.execute("""
UPDATE airport
SET code = 'MUM'
WHERE airport_id = 3  
""")
conn.commit()

# display changes
mycursor.execute("SELECT * FROM flights.airport")
data = mycursor.fetchall()
print(data)

#########################################
# Delete entry
mycursor.execute("DELETE FROM airport WHERE airport_id = 2")
conn.commit()

# display changes
mycursor.execute("SELECT * FROM flights.airport")
data = mycursor.fetchall()
print(data)