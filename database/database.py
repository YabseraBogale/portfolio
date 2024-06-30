import sqlite3

class Database():
    
    def __init__(self):
        self.connection=sqlite3.Connection("database.db")
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
            return repr(e)
        