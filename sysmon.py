import psutil 
import time 
import os 

def print_info():

	#reset screen 
    os.system('clear')

    #create som space 
    for i in range(3):
    	print(' ')

    #CPU#######
    cpu_pct = psutil.cpu_percent()
    print('    CPU useage  ::  {}%'.format(cpu_pct))
    cpu_freq = psutil.cpu_freq()[0]/1000
    print('    CPU freq    ::  {:.1f}Ghz'.format(cpu_freq))
    print(' ')
    
    #get cpu die temp 
    cpu_temp = 'error'
    dct = psutil.sensors_temperatures()
    for lst in dct.get('k10temp'):
        if lst[0]=='Tdie':
            cpu_temp = lst[1]
    print('    CPU temp    ::  {:.0f}C'.format(cpu_temp))
    print(' ')
    
    #Memory###
    print('    RAM total   ::  {:.0f}GB'.format(psutil.virtual_memory()[0]/1000000000))
    print('    RAM used    ::  {:.0f}GB'.format(psutil.virtual_memory()[3]/1000000000))
    print('    RAM used %  ::  {:.0f}%'.format(psutil.virtual_memory()[2]))

    #more space 
    for i in range(4):
    	print(' ')
    
 

while(True):
	print_info()
	time.sleep(2)
