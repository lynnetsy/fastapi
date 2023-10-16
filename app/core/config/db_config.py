class DbConfig:
    def __init__(self, engine: str, host: str, port: str, db_name: str, user: str, password: str) -> None:
        self.engine = engine
        self.host = host
        self.port = port
        self.db_name = db_name
        self.user = user
        self.password = password
        self.url = self.get_url()

    def get_url(self):
        if self.engine == "postgres":
            return self.get_postgres_url()

        elif self.engine == "sqlite":
            return self.get_sqlite_url()


    def get_postgres_url(self):
        return "postgresql+asyncpg://%s:%s@%s:%s/%s" % (
            self.user,
            self.password,
            self.host,
            self.port,
            self.db_name
        )

    def get_sqlite_url(self):
        pass
