#DB選択
USE PMDB;

#M020
DROP TABLE M020_MSGMST;
CREATE TABLE M020_MSGMST (
	MSGID char(5) NOT NULL PRIMARY KEY,
	MSGLEVEL varchar(10)NOT NULL,
	MSGNAIYO varchar(512)NOT NULL,
	CRTSRV char(5) NOT NULL,
	CRTUSR char(18) NOT NULL,
	CRTDATE DATETIME(6) NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR char(18) NOT NULL,
	UPDDATE DATETIME(6) NOT NULL,
	DELFLG char(1) NOT NULL
);