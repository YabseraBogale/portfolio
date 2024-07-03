import sqlite3

class Database():
    
    def __init__(self):
        self.connection=sqlite3.connect("database.db")
        self.pointer=self.connection.cursor()
    def InsertIntoProject(self,projectName,projectDescripition):
        try:
            statment="Insert into project(projectName,projectDescripition) values(?,?)"
            self.pointer.execute(statment,(projectName,projectDescripition,))
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)
    
    