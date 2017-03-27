import paramiko
import time
import os


user = 'user'    #Create a read only admin user to pull configs.  That user name goes here.
password = 'password'    #Password for the user listed above
switchip = 'deviceip'    #IP address of your ZoneDirector
wikipath = '/path/to/dokuwiki/pages/directory'    #Path to your local dokuwiki install, including the trailing slash Eg. /opt/dokuwiki/data/pages/
filename = 'namethefileyouwantthescripttocreate.txt'    #Name of the file you want to reference in dokuwiki

#Change to dokuwiki path

os.chdir(wikipath)

#If there's an existing config file in dokuwiki delete it

if os.path.isfile(filename):
    os.remove(wikipath + filename)

#Establish a ssh connection to the ZoneDirector.  ***Please note that the ZoneDirector has an interactive logon session for ssh connections, the password field should be blank*** 

paramiko.util.log_to_file("filename.log")
precon = paramiko.SSHClient()
precon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
precon.connect(switchip, username=user, password='')

#Invoke ssh shell

con = precon.invoke_shell()

#Send user and wait

con.send(user + '\n')
time.sleep(3)

#Send password and wait

con.send(password + '\n')
time.sleep(3)

#Enter enabled mode and wait

con.send('en\n')
time.sleep(3)

#Send "show techsupport" command and wait for output to complete

con.send('show techsupport\n')
time.sleep(30)

#Write config to file along with the <code></code> at the beginning/end of file to avoid formatting issues

configfile = open(wikipath + filename, 'w')
configfile.write('<code>')
configfile.write('\n\n\n')
configfile.write(con.recv(10000000))
configfile.write('\n\n\n</code>\n\n\n\n')
configfile.close()

#Change owner and group of file to www-data:www-data so that apache can access it (You'll need to make sure you know the user and group number for www-data)

os.chown(wikipath + filename, 33, 33)

#Close ssh session

precon.close()
