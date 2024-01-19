from libs.postgresql import Postgres

class Querys(Postgres):
    __GET__ = 'select {} from {} '
    __INSERT__ = 'insert into {} ({}) '
    __VALUES_INSERT__ = 'VALUES %s'
    __WHERE__ = 'where {}'
    __SCHEMA__ = "select column_name from information_schema.columns where table_name = '{}'" #  NOQA

    def fetchall(self, values: dict={}, key:str='id'):
        sql = self.__GET__.format(key, self.__table__)

        if values:
            if isinstance(values, dict):
                where = ','.join([
                    f"{k} = '{v}'" for k,v in values.items()
                ])
                sql = sql + self.__WHERE__.format(where)
            
        return super()._fetchall(sql)
    
    def insert(self, keys: str, values:list):

        if values:

            sql = self.__INSERT__.format(self.__table__, keys)
            sql = sql + self.__VALUES_INSERT__

            resp = super()._insert(sql, values)

            return resp