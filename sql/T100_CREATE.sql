#DB選択
USE PMDB;

#T100
DROP TABLE T100_PROJECT;
CREATE TABLE T100_PROJECT (
	PROJECTID char(18) NOT NULL PRIMARY KEY,
	URLID varchar(256) NOT NULL,
	PROJECTNAME varchar(256) ,
    PROJECT_COMMENT varchar(256) ,
    PROJECT_NAIYO varchar(65535) ,
	PROJECT_CRTUSER char(18) NOT NULL,
	CRTSRV char(5) NOT NULL,
	CRTUSR char(18) NOT NULL,
	CRTDATE DATETIME NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR char(18) NOT NULL,
	UPDDATE DATETIME NOT NULL,
	DELFLG char(1) NOT NULL
);