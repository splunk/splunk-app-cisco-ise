import time,sys,os,traceback,random

## Define the events per second
EPS = 1

## Get common app vars, IPS's, sigs, etc. 
libPath = os.path.join(os.environ["SPLUNK_HOME"], 'etc','apps','Splunk_CiscoISE','bin','Cisco_ISE_datagen')

# Initialze vars
int_ips = open(os.path.join(libPath,'data','internal_addresses.txt')).readlines()
int_users = open(os.path.join(libPath,'data','internal_users.txt')).readlines()

## Get required log samples 
log_sample  = open(os.path.join(libPath,'data','cisco_ise_sample.log'),'r').readlines()


## Define output log
log_out = open(os.path.join(libPath,'data','cisco_ise_ouput.log'),'w')

def getCurrentEvent(evt):
	int_ip = int_ips[random.randint(0,len(int_ips)-1)].replace("\n","")
	ts = time.time()
	device_ip = evt.find('Device\sIP\sAddress\=(?<device_ip>\d+\.\d+\.\d+\.\d+)')
	line  =  str(ts) + evt[evt.find('Device\sIP\sAddress\=\d+\.\d+\.\d+\.\d+'):].replace('',int_ip)
	return line
	

while True:
	e = 0
	for line in log_sample:
		if e < EPS:
			l = getCurrentEvent(line)
			log_out.writelines(l)
			log_out.flush()	
			e = e + 1
		else:
			e = 0 
			l = getCurrentEvent(line)
			log_out.writelines(l)
			log_out.flush()	
			time.sleep(1)



