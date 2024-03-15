from json import loads
from os import getcwd, path

__CONFIG_FILE__ = path.join(getcwd(), 'config.json')

class Credentials():
    def __init__(self) -> None:
        self._cred()
    
    def _cred(self):
        with open( __CONFIG_FILE__ , 'r+') as file:
            out = file.read()
            self.__DB__ = loads(out).get('psql')
            self.__APP__ = loads(out).get('app')
            self.__SECRET__ = loads(out).get('secret')
            self.__AUTH_TEST__ = loads(out).get('auth')
        
            file.close()
        return