CREATE TABLE IF NOT EXISTS Ganre (
GanreID SERIAL PRIMARY KEY,
Ganre_name VARCHAR(40)
) ;

CREATE TABLE IF NOT EXISTS Author (
AuthorID SERIAL PRIMARY KEY,
nickname VARCHAR(30)
) ;

CREATE TABLE IF NOT EXISTS GanreAuthor (
GanreID INTEGER REFERENCES Ganre(GanreID),
AuthorID INTEGER REFERENCES Author(AuthorID),
CONSTRAINT pk PRIMARY KEY (GanreID, AuthorID)
) ;

CREATE TABLE IF NOT EXISTS Albums (
AlbumID SERIAL PRIMARY KEY ,
name_album VARCHAR(30),
date_realise date
) ;

CREATE TABLE IF NOT EXISTS AuthorAlbums (
AuthorID INTEGER REFERENCES Author(AuthorID),
AlbumID INTEGER REFERENCES Albums(AlbumID),
CONSTRAINT pc PRIMARY KEY (AuthorID, AlbumID)
) ;

CREATE TABLE IF NOT EXISTS Track (
songID SERIAL PRIMARY KEY,
name_track VARCHAR(20),
AlbumID SERIAL NOT NULL REFERENCES Albums(AlbumID)
) ;

CREATE TABLE IF NOT EXISTS Collection (
collectionID SERIAL PRIMARY KEY,
name_collection VARCHAR(20),
realise date
) ;

CREATE TABLE IF NOT EXISTS CollectionTrack (
collectionID INTEGER REFERENCES Collection(collectionID),
songID INTEGER REFERENCES Track(songID),
CONSTRAINT ps PRIMARY KEY (collectionID, songID)
) ;