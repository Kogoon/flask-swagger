from database import Database
import json
import utils


#
# For RandomTable
# 
class RandomTable(Database):

    # For Get data by ID
    def get(self, id):
    
        sql = "SELECT * FROM wp_random "
        sql += "WHERE id={};".format(id)
        print("DEBUG SQL ==> {}".format(sql))

        result = ()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return {"error" : "{}".format(e)}

        result = {} if len(result) == 0 else result[0]

        return result


    # For Get All Data
    def list(self, page=0, itemsInPage=20):
        
        page = page * itemsInPage
        sql =  "SELECT id, random FROM wp_random "
        sql += "LIMIT {p}, {item};".format(p=page, item=itemsInPage)
        print("DEBUG SQL ===> {}".format(sql))
        
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result


    def count(self):

        sql = "SELECT random FROM wp_random;"
        print("DEBUG SQL ===> {}".format(sql))

        self.cursor.execute(sql)
        self.cursor.fetchall()
        result = self.cursor.rowcount

        return result


    # For Insert
    def insert(self, value):
        
        sql =  "INSERT INTO wp_random(random) "
        sql += "values('{random}')".format(random=value)
        print("DEBUG SQL ===> {}".format(sql))
        
        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"error" : "{}".format(e)}
        
        return result


    # For Update
    def update(self, id, j):
        
        u_random = j.get("random", "")

        sql =  "UPDATE wp_random SET "
        if u_random is not None: 
            sql += "random = '{}' ".format(u_random)
        else:
            return "error"
        sql += "WHERE id = {}".format(id)
        print("DEBUG SQL ===> {}".format(sql))

        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"error" : "{}".format(e)}

        return result


    # For Delete
    def delete(self, id):
        
        sql = "DELETE FROM wp_random "
        sql += "WHERE id='{}'".format(id)
        

        print("DEBUG SQL ==> {}".format(sql))
        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"error" : "{}".format(e)}

        return result


    def deleteAll(self):

        sql = "DELETE FROM wp_random;"
        
        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
            sql = "ALTER TABLE wp_random AUTO_INCREMENT=1;"
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"error":"{]".format(e)}

        return result
