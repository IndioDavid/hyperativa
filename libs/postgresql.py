import psycopg2
from credetions import Credetions


class Postgres():
    def _conn(self):
        return psycopg2.connect(**Credetions().__DB__)
    
    def _fetchall(self, sql):
        resp = []

        db = self._conn()
        cursor = db.cursor()
        cursor.execute(sql)
        try:
            for row in cursor.fetchall():
                resp.append({
                    'id': row[0]
                })
            cursor.close()
            return resp
        except Exception as e:
            return {'status_code': 500, 'state': 'ERROR', 'msg': str(e)}


    def _insert(self, sql):

        db = self._conn()
        
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            db.close()
            return {'status_code': 200, 'state': 'SUCCESS', 'msg': 'insert with success'}
        
        except psycopg2.errors.UniqueViolation as e:
            db.rollback()
            db.close()
            return {'status_code': 409, 'state': 'ERROR', 'msg': str(e)}

        except Exception as e:
            db.rollback()
            db.close()
            return {'status_code': 500, 'state': 'ERROR', 'msg': str(e)}

    def update(self):
        pass

    def delete(self):
        pass

