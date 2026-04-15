import pymysql

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               db='courses',
                               cursorclass=pymysql.cursors.DictCursor)
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()

    def execute(self, sql, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def fetchall(self, sql, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def fetchone(self, sql, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchone()
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

db = Database()