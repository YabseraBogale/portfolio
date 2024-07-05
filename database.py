from random import randint
import sqlite3

class Database():
    
    def __init__(self):
        self.connection=sqlite3.connect("database.db",check_same_thread=False)
        self.pointer=self.connection.cursor()

    def CreateTableProject(self):
        try:
            statment="create table if not exists project(projectName varchar(50) not null,projectDescripition Text not null)"
            self.pointer.execute(statment)
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)

    def CreateTableUriShortener(self):
        try:
            statment="create table if not exists UriShortener(orginalUri Text not null UNIQUE, newUri varchar(5) not null UNIQUE,numberOfUse int not null)"
            self.pointer.execute(statment)
            self.connection.commit
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
    
    def InsertUriShortener(self,uri):
        try:
            newuri=chr(randint(97,122))+chr(randint(97,122))+chr(randint(97,122))+chr(randint(97,122))+chr(randint(97,122))
            statment="insert into UriShortener(orginalUri,newUri,numberOfUse) values(?,?,?)"
            self.pointer.execute(statment,(uri,newuri,1))
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)
    
    def GetSpecificUri(self,orginalUri):
        try:
            statment="select newUri from UriShortener where orginalUri=?"
            self.pointer.execute(statment,(orginalUri,))
            self.result=self.pointer.fetchone()
            return self.result
        except Exception as e:
            return str(e)

    def GetAllProject(self):
        try:
            self.pointer.execute("select * from project")
            self.result=self.pointer.fetchall()
            return self.result
        except Exception as e:
            return str(e)



