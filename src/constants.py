class Loglevel:
    STRING: str = 'NOTSET'
    INT: int = 0


class NOTSET(Loglevel):
    STRING: str
    INT: int


class DEBUG(Loglevel):
    STRING: str = 'DEBUG'
    INT: int = 10


class INFO(Loglevel):
    STRING: str = 'INFO'
    INT: int = 20


class WARNING(Loglevel):
    STRING: str = 'WARNING'
    INT: int = 30


class ERROR(Loglevel):
    STRING: str = 'ERROR'
    INT: int = 40


class CRITICAL(Loglevel):
    STRING: str = 'CRITICAL'
    INT: int = 50
