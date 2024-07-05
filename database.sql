create table if not exists project(
    projectName varchar(50) not null,
    projectDescripition Text not null
)

create table if not exists UriShortener(
    orginalUri Text not null,
    newUri varchar(5) not null,
    numberOfUse int not null
)