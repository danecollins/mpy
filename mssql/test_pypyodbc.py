import pypyodbc
import getpass

uid=r'ni\dcollins'
pwd=getpass.getpass()

cnxn = pypyodbc.connect('DRIVER=FreeTDS;SERVER=db2a;PORT=1433;DATABASE=ccmast;UID={};PWD={};'.format(uid, pwd))
cursor = cnxn.cursor()
cursor.execute("select * from lds_ip_history where entered_date > '2015-10-28'")
for r in cursor.fetchall():
    print(r)
