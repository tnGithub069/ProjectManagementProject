#DB選択
USE PMDB;

#詳細1件
select PROJECTID,URLID,PROJECTNAME,PROJECT_NAIYO,PROJECT_CRTUSER,CRTDATE,UPDDATE from T100_PROJECT where SHITSMN_ID = "Q20210920000000001" ;

#リスト
select PROJECTID,URLID,PROJECTNAME,PROJECT_NAIYO,PROJECT_CRTUSER,CRTDATE,UPDDATE  from T100_PROJECT order by PROJECTID ASC ;
