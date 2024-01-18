from json import loads

class Credetions:
    __DB__ = {}
    __APP__ = {}
    def __init__(self) -> None:
        self._cred()
    
    def _cred(self):
        with open('config.json', 'r+') as file:
            out = file.read()
            self.__DB__ = loads(out)['psql']
            self.__APP__ = loads(out)['app']
            file.close()
        return