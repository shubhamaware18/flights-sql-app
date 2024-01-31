import mysql.connector

class DB:
    def __init__(self):
        # Connect to the database server
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database='flights',
                auth_plugin='mysql_native_password'
            )
            
            self.mycursor = self.conn.cursor()
            print('Connection Established')
        except mysql.connector.Error as e:
            print(f'Connection Error: {e}')

    def fetch_city_names(self):
        """
        Fetches a list of city names from the database.

        This function connects to the database and retrieves a list of unique city names
        stored in the 'cities' table.

        Returns:
        - A list of strings representing the names of cities in the database.

        Raises:
        - DatabaseConnectionError: If there is an issue connecting to the database.
        - QueryExecutionError: If there is an error executing the SQL query.
        """

        # creating exmpty list for cities
        city = []

        try:
            # Writing a Query to get distinct cities from the database
            self.mycursor.execute("""
                    SELECT DISTINCT(Destination) FROM flights.flight
                                  UNION
                    SELECT DISTINCT(Source) FROM flights.flight        
                                """)
            # Storing the result in the data variable
            data = self.mycursor.fetchall()
            #print(data)
            #return data
    
            for item in data:
                city.append(item[0])
            
            # returning cities
            return city
        except mysql.connector.Error as query_error:
            # Handle specific query-related errors
            print(f"Query Execution Error: {query_error}")
            raise QueryExecutionError("Error executing SQL query.")

        # finally:
        #     # Close the cursor and connection
        #     self.mycursor.close()
        #     self.conn.close()

# Custom exception for database connection errors
class DatabaseConnectionError(Exception):
    pass

# Custom exception for query execution errors
class QueryExecutionError(Exception):
    pass
