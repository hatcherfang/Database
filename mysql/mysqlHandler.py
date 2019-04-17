import MySQLdb
from DBUtils.PooledDB import PooledDB
import logging
import time
import traceback


class MySQL(object):
    '''mysql interfaces handler''' 
    def __init__(self, host="localhost", username="root", 
                 password="root", database="", 
                 port=3306, 
                 mincached=1, maxcached=1):
        '''
         mincached: minimum free connection number
         maxcached: maximum free connection number
        '''
        pool = PooledDB(MySQLdb, 
                        mincached=mincached,
                        maxcached=maxcached,
                        host=host, 
                        user=username, 
                        passwd=password, 
                        db=database, 
                        port=port) 
        self.conn = pool.connection()
    
    def lockTable(self, cur, tableName, operation):
        '''
        function: lock table by tableName
        cur: cursor
        operation: WRITE/READ
        '''
        try:
            lockSQL="LOCK TABLES %s %s" % (tableName, operation)
            cur.execute(lockSQL)
        except Exception as e:
            logging.error("e:%r, traceback:%r", e, traceback.print_exc())
            print e, traceback.print_exc()

    def unlockTable(self, cur):
        '''
        function: unlock table 
        '''
        try:
            unlockSQL="UNLOCK TABLES"
            cur.execute(unlockSQL)
        except Exception as e:
            logging.error("e:%r, traceback:%r", e, traceback.print_exc())
            print e, traceback.print_exc()

    def createTable(self, sql):
        '''
        function: create table
        rtype: bool
        '''
        try:
            ret = True
            cur = self.conn.cursor()
            cur.execute(sql)
        except Exception as e:
            logging.error("e:%r, traceback:%r", e, traceback.print_exc())
            print e, traceback.print_exc()
            ret = False
        finally:
            cur.close()
        return ret

    def query_withoutlock(self, sql):
        '''
        function: query data by sql
        return: the data stored in mysql
        '''
        try:
            ret = None
            cur = self.conn.cursor()
            cur.execute(sql)
            ret = cur.fetchall()
        except Exception as e:
            logging.error("e:%r, traceback:%r", e, traceback.print_exc())
            print e, traceback.print_exc()
        finally:
            cur.close()
        return ret

    def query(self, sql, tableName):
        '''
        function: query data by sql
        return: the data stored in mysql
        '''
        try:
            ret = None
            cur = self.conn.cursor()
            self.lockTable(cur, tableName, "READ")
            cur.execute(sql)
            ret = cur.fetchall()
        except Exception as e:
            logging.error("e:%r, traceback:%r", e, traceback.print_exc())
            print e, traceback.print_exc()
        finally:
            self.unlockTable(cur)
            cur.close()
        return ret

    def insert(self, sql, tableName):
        ''' 
        function: insert data into mysql by sql
        return: 0 <-> insert failed or insert succeed
        '''
        try:
            ret = 0
            cur = self.conn.cursor()
            self.lockTable(cur, tableName, "WRITE")
            ret = cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logging.error("e:%r, traceback:%r", e, traceback.print_exc())
            print e, traceback.print_exc()
            if self.conn:
                self.conn.rollback()
            ret = 0
        finally:
           self.unlockTable(cur)
           cur.close()
        return ret

    def delete(self, sql):
        '''
        function: delete data by sql
        return: 0 <-> delete failed or delete succeed
        '''
        try:
            ret = 0 
            cur = self.conn.cursor()
            ret = cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logging.error("e:%r, traceback:%r", e, traceback.print_exc())
            print e, traceback.print_exc()
            if self.conn:
                self.conn.rollback()
            ret = 0
        finally:
           cur.close()
        return ret

if __name__ == '__main__':
    pass
