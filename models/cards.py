from .querys import Querys
from libs.postgresql import Postgres

class Card(Querys, Postgres):
    __table__ = 'cards'

    def fetchall(self, values: dict):
        sql = self.__GET__.format('id', self.__table__)

        if values:
            if isinstance(values, dict):
                where = ','.join([
                    f"{k} = '{v}'" for k,v in values.items()
                ])
                sql = sql + self.__WHERE__.format(where)
            
        return super()._fetchall(sql)
    
    def insert(self, keys: str, values:list):

        if values:
            for v in values:
                resp = Postgres()._insert(
                    self.__INSERT__.format(
                        self.__table__, 
                        keys, 
                        v
                    )
                )
                if resp.get('out') == 'error':
                        return resp
            return resp
                
                    
