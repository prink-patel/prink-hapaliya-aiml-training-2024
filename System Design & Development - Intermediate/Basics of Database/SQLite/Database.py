import sqlite3


class Database:
    def __init__(self, database_name):
        self.database_name = database_name

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.database_name)
            self.cursor = self.conn.cursor()
            print("Database connected successfully")
        except sqlite3.OperationalError:
            print("Database already exists")

    def disconnect(self):

        self.cursor.close()

    def Create_table(self, table_name, query):
        self.table_name = table_name
        try:
            self.cursor.execute(f"CREATE TABLE {self.table_name} ({query})")
        except sqlite3.OperationalError:
            print("Table already exists")

    def Add_single_row(self, query):
        try:
            self.cursor.execute(f"INSERT INTO {self.table_name} VALUES ({query})")
        except sqlite3.OperationalError:
            print("Table doesn't exist")

    def Add_multiple_row(self, query) -> None:
        try:
            for query_row in query:
                self.cursor.execute(f"INSERT INTO Users VALUES {query_row}")
        except sqlite3.OperationalError:
            print("Table doesn't exist")

    def get_user_by_id(self, id):
        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE Id = {id}")
            output = self.cursor.fetchall()
            self.print_(output)
        except sqlite3.OperationalError as e:
            print(e)

    def update_user_name_by_email(self, email, new_username):
        try:
            self.cursor.execute(
                f"UPDATE {self.table_name} SET User_Name = '{new_username}' WHERE Email = '{email}'"
            )
        except sqlite3.OperationalError as e:
            print(e)

    def delete_user_by_id(self, id):
        try:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE Id = {id}")
        except sqlite3.OperationalError as e:
            print(e)

    def print_(self, parameter):
        try:
            for row in parameter:
                print(row)
        except:
            print("output doesn't exist")

    def get_all_users(self):
        try:
            data = self.cursor.execute(f"SELECT * FROM {self.table_name}")
            for row in data:
                print("----------")
                print(row)
        except:
            print("table value doesn't exist")
            
            
            
database_name = "Database.db"
table_name = "Users"
query = """ Id INT NOT NULL,User_Name CHAR(25) NOT NULL, Contact_Number INT, Email VARCHAR(255) unique """
Add_Single_row = " 1, 'abc', '1234567890', 'abc@123'"

Add_multiple_row = [
    (2, "xyz", "1234547890", "xyz@123"),
    (3, "zyx", "1234567490", "zyx@123"),
    (4, "cde", "1534767590", "cde@123"),
]

user_id = 2


Database = Database(database_name)
Database.connect()
Database.Create_table(table_name, query)
Database.Add_single_row(Add_Single_row)
Database.Add_multiple_row(Add_multiple_row)
Database.get_user_by_id(user_id)
Database.update_user_name_by_email("abc@123", "xyz1")
Database.delete_user_by_id(user_id)
Database.get_all_users()
Database.disconnect()