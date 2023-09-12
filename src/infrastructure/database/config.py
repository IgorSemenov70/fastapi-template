from dataclasses import dataclass


@dataclass
class DBConfig:
    """Data class for holding database configuration.

    This class defines a data structure to hold configuration parameters for a database connection.

    Attributes:
        host (str): The host of the database server. Default is "localhost".
        port (int): The port number for the database server. Default is 5432.
        database (str): The name of the database to connect to. Default is "test".
        user (str): The username for authentication. Default is an empty string.
        password (str): The password for authentication. Default is an empty string.
        echo (bool): Whether to enable query logging. Default is True.
    """

    host: str = "localhost"
    port: int = 5432
    database: str = "prod_db"
    user: str = "admin"
    password: str = "admin"
    echo: bool = True

    @property
    def full_url(self) -> str:
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.database,
        )
