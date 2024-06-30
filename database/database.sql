create table if not exists Article(
    ArticleName varchar(50) not null primary key,
    ArticleDate datetime not null,
    TimeToFinish int not null
)