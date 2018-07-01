from netmiko import ConnectHandler
import getpass
from datetime import datetime
user_name = raw_input('Please enter .web username ')
pwd = getpass.getpass('Enter .web Password: ')
#host_list = raw_input('Please enter hostname/hostnames saperated by comma: ')
#cmd_45 = 'show  version | sec Last reload reason'
show_cmd = 'show  version | sec Last reload reason' 
# more line in comments
#if ',' in host_list:
#    host_list= host_list.split(',')
#else:
#    host_list= [host_list]

#host_list = open(list)
#list = open('routerlist')

with open('routerlist') as f:
    content = f.readlines()

content = [x.strip() for x in content]
host_list = content
for host in host_list:
    print "Connecting to device %s with cerdentials of %s" %(host,user_name)
    cisco = {'device_type': 'cisco_ios','ip': host ,'username': user_name ,'password':pwd}
    ssh_conn = ConnectHandler(**cisco)
    if ssh_conn.check_enable_mode() == True:
        print 'logged into the device and we are in enable prompt !'
    else:#
        print 'Ops !! something wrong with the password of %s, pls try again !!' %username
    print "preparing the details for the audit"
#    sh_cmd_45 = ssh_conn.send_command(cmd_45)
#    print "****************************"
#    print host
#    if not sh_cmd_45:
#        print "not ASR router, can you pls crosscheck again !!!"
#    else:
    sh_mem_output = ssh_conn.send_command(show_cmd)

    sh_mem_output = ssh_conn.send_command(show_cmd)
#        sh_mem_outputlines = sh_mem_output.splitlines()[4]
#        sh_mem_outputcontent = sh_mem_outputlines.split()[0] +" free_space " + sh_mem_outputlines.split()[4]
    print sh_mem_output
    ssh_conn.disconnect()
    print "****************************"
    print "Script Completed"
