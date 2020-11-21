from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


while True:

    rack_num = input('''
                                <----------Enter the Rack number--------->
                                                          1 for rack1 
                                                          2 for rack2 
                                                          3 for rack3 
                                                          4 for rack4 
                                                          5 for rack5
                                                          0 to exit
                                                          Enter the rack_num for ON/OFF unit : ''')
    
    if(int(rack_num) == 1):
        import Rack_1_ONOFF
        continue
    elif(int(rack_num) == 2):
        import Rack_2_ONOFF
        continue
    elif(int(rack_num) == 3):
        import Rack_3_ONOFF
        continue
    elif(int(rack_num) == 4):
        import Rack_4_ONOFF
        continue
    elif(int(rack_num) == 5):
        import Rack_5_ONOFF
        continue
    else:
        print("Exiting Loop")
    break
    
