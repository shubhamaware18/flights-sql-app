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

    # creating new method for fetching all Flights
    def fetch_all_flights(self, source, destination):
        """
        This function is responsible for fetching flights based on source and destination.
        """
        try:
            # Using parameterized query to prevent SQL injection
            query = """
                SELECT Airline, Route, Dep_time, Duration, Price
                FROM flights.flight
                WHERE Source = %s AND Destination = %s
            """
            self.mycursor.execute(query, (source, destination))

            data = self.mycursor.fetchall()
            return data
        except mysql.connector.Error as query_error:
            # Handle specific query-related errors
            print(f"Query Execution Error: {query_error}")
            raise QueryExecutionError("Error executing SQL query.")


    # method for data visualization of Pie chart
    def fetch_airline_frequency(self):
        
        """
        This method fetch  the flights and its frequency
        """
        # creating empty lists for results(airline anme and frequency)
        airline = []
        frequency = []
        
        # SQL Query to fetch results
        self.mycursor.execute("""
            SELECT Airline, COUNT(*) FROM flights.flight
                        GROUP BY Airline
                                """)
        data = self.mycursor.fetchall()

        for item in data:
            # appending results to respective lists
            airline.append(item[0])
            frequency.append(item[1])
        
        return airline, frequency
    

    # method for data visualization of Bar Plot
    def busy_airport(self):
        # creating empty lists for results(City anme and frequency)
        city = []
        frequency = []

        self.mycursor.execute("""
            SELECT Source, COUNT(*) FROM (SELECT Source FROM flights.flight
                              UNION ALL
                              SELECT Destination FROM  flights.flight) t
            GROUP BY t.Source
            ORDER BY COUNT(*) DESC""")
        
        data = self.mycursor.fetchall()

        for item in data:
            # appending results to respective lists
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency
    

    # method for data visualization of Line chart
    def daily_frequency(self):
        # creating empty lists for results(date anme and frequency)
        date = []
        frequency = []

        self.mycursor.execute("""
            SELECT Date_of_Journey, COUNT(*) FROM flights.flight
                        GROUP BY Date_of_Journey
                                """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency
    
# Custom exception for database connection errors
class DatabaseConnectionError(Exception):
    pass

# Custom exception for query execution errors
class QueryExecutionError(Exception):
    pass
