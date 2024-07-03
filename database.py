import sqlite3

class Database():
    
    def __init__(self):
        self.connection=sqlite3.connect("database.db")
        self.pointer=self.connection.cursor()

    def CreateTableProject(self):
        try:
            statment="create table if not exists project(projectName varchar(50) not null,projectDescripition Text not null)"
            self.pointer.execute(statment)
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)

    def InsertIntoProject(self,projectName,projectDescripition):
        try:
            statment="Insert into project(projectName,projectDescripition) values(?,?)"
            self.pointer.execute(statment,(projectName,projectDescripition,))
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)
    
    def GetAllProject(self):
        try:
            self.pointer.execute("select * from project")
            self.result=self.pointer.fetchall()
            return self.result
        except Exception as e:
            return str(e)



