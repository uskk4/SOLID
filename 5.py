from abc import ABC, abstractmethod

class Database(ABC):
    """
    Абстрактний інтерфейс для баз даних.
    """
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLDatabase(Database):
    """
    Реалізація для MySQL.
    """
    def connect(self):
        print("Connecting to MySQL database...")

    def execute_query(self, query):
        print(f"Executing query on MySQL: {query}")


class PostgreSQLDatabase(Database):
    """
    Реалізація для PostgreSQL.
    """
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def execute_query(self, query):
        print(f"Executing query on PostgreSQL: {query}")


class DataProcessor:
    """
    Клас, який обробляє дані.
    """
    def __init__(self, database: Database):
        self.database = database  # Залежність через абстракцію

    def process_data(self):
        self.database.connect()
        self.database.execute_query("SELECT * FROM data")


# Використання
mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

processor1 = DataProcessor(mysql_db)
processor2 = DataProcessor(postgresql_db)

# Обробка даних з MySQL
processor1.process_data()

# Обробка даних з PostgreSQL
processor2.process_data()
