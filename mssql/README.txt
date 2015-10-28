On the mac use FreeTDS
mac installation is based on brew
	see: https://gist.github.com/tommct/5749453

seems like you also have to
brew install unixodbc
brew install openssl
brew install freetds --with-unixodbc

.odbc.ini
--------------
[AWRDB]
Driver = FreeTDS
Server = db2a
Port = 1433

.odbcinst.ini
----------------------------
[FreeTDS]
Driver = /usr/local/lib/libtdsodbc.so
Setup = /usr/local/lib/libtdsodbc.so
FileUsage = 1

Testing
-----------------------------------------------------------------------
step 1
	tsql -H db2a -p 1433 -U 'ni\dcollins' -P passwd
	1> use ccmast
	2> go
	1> select * from lds_ip_history where entered_date > '2015-10-25'
	2> go
	1> exit

step 2
	isql AWRDB 'ni\dcollins' Ak6nc6uu55 -vvvv

step 3
	python mpy/mssql/test.py

Connect String
--------------
pyodbc.connect('DRIVER=FreeTDS;SERVER=db2a;PORT=1433;DATABASE={};UID={};PWD={};'.format(database, uid, pwd))

DEBUGGING HELP:
	http://stefanoapostolico.com/2015/04/20/django_mssql_osx.html