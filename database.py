import sqlite3

class Database():
    
    def __init__(self):
        self.connection=sqlite3.connect("database.db")
        self.pointer=self.connection.cursor()

    def InsertIntoArticle(self,ArticleName,ArticleDate,TimeToFinish):
        try:
            statment="Insert into Article(ArticleName,ArticleDate,TimeToFinish)values(?,?,?)"
            self.pointer.execute(statment,(ArticleName,ArticleDate,TimeToFinish))
            self.connection.commit()
            return True
        except Exception as e:
            return repr(e)
    
    def GetArticle(self):
        try:
            self.pointer.execute("select * from Article")
            self.result=self.pointer.fetchall()
            return True
        except Exception as e:
            return str(e)


Database().CreateArticle()
Database().InsertIntoArticle("hello world","12-2-1024","12-2-1024")
print(Database().GetArticle())