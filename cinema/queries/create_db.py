DROP_USER = """
	DROP TABLE IF EXISTS USER
"""
DROP_MOVIES = """
	DROP TABLE IF EXISTS MOVIES
"""
DROP_PROJECTIONS = """
	DROP TABLE IF EXISTS PROJECTIONS
"""
DROP_RESERVATIONS = """
	DROP TABLE IF EXISTS RESERVATIONS
"""


CREATE_USER = """
	CREATE TABLE IF NOT EXISTS USER(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		USERNAME TEXT NOT NULL,
		PASSWORD TEXT NOT NULL
	)
"""
CREATE_MOVIES = """
	CREATE TABLE IF NOT EXISTS MOVIES(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NAME TEXT,
		RATING INTEGER
	)
"""
CREATE_PROJECTIONS = """
	CREATE TABLE IF NOT EXISTS PROJECTIONS(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		MOVIE_ID INTEGER,
		TYPE TEXT,
		DATE TEXT,
		TIME TEXT,
		FOREIGN KEY (MOVIE_ID) REFERENCES MOVIES(ID)  
	)
"""
CREATE_RESERVATIONS = """
	CREATE TABLE IF NOT EXISTS RESERVATIONS(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		USER_ID INTEGER,
		PROJECTION_ID INTEGER,
		ROW INTEGER,
		COL INTEGER,
		FOREIGN KEY (USER_ID) REFERENCES USER(ID),
		FOREIGN KEY (PROJECTION_ID) REFERENCES PROJECTIONS(ID)
	)
"""

INSERT_USER = """
	INSERT INTO USER(USERNAME,PASSWORD)
	VALUES(?, ?)
"""
INSERT_MOVIES = """
	INSERT INTO MOVIES(NAME, RATING)
	VALUES(?, ?)
"""
INSERT_PROJECTIONS = """
	INSERT INTO PROJECTIONS(TYPE, DATE, TIME)
	VALUES(?, ?, ?)
"""
INSERT_RESERVATIONS = """
	INSERT INTO RESERVATIONS(USER_ID, PROJECTION_ID, ROW, COL)
	VALUES(?, ?, ?, ?)
"""


