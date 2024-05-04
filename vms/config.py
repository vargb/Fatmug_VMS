from typing import Any
from dataclasses import dataclass
import json
import logging
import os

loggy = logging.getLogger(__name__)


@dataclass
class Postgres:
    host: str
    sqlport: str
    user: str
    password: str
    dbname: str

    @staticmethod
    def from_dict(obj: Any) -> "Postgres":
        _host = str(obj.get("host"))
        _sqlport = str(obj.get("port"))
        _user = str(obj.get("username"))
        _password = str(obj.get("password"))
        _dbname = str(obj.get("dbname"))
        return Postgres(_host, _sqlport, _user, _password, _dbname)


@dataclass
class Server:
    host: str
    port: str

    @staticmethod
    def from_dict(obj: Any) -> "Server":
        _host = str(obj.get("host"))
        _port = str(obj.get("port"))
        return Server(_host, _port)


@dataclass
class Root:
    server: Server
    postgres: Postgres

    @staticmethod
    def from_dict(obj: Any) -> "Root":
        _server = Server.from_dict(obj.get("server"))
        _postgres = Postgres.from_dict(obj.get("postgres"))
        return Root(_server, _postgres)


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "config.json")) as config_file:
    parsed_json = json.load(config_file)
conf = Root.from_dict(parsed_json)
loggy.info("parsing of config file is done")

postgresUrl = (
    "postgresql://"
    + conf.postgres.user
    + ":"
    + conf.postgres.password
    + "@"
    + conf.postgres.host
    + ":"
    + conf.postgres.sqlport
    + "/"
    + conf.postgres.dbname
)
