
class Querys:
    __GET__ = 'select {} from {} '
    __INSERT__ = 'insert into {} ({}) values ({})'
    __WHERE__ = 'where {}'
    __SCHEMA__ = "select column_name from information_schema.columns where table_name = '{}'"