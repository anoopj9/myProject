from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Python37\Scripts\chromedriver.exe')

class rack_3:
    rack3_url_index1 = 'http://10.107.74.150/index1.htm'
    rack3_url_index2 = 'http://10.107.74.150/index2.htm'
    rack3_cntrl_out = '//*[@id="control1"]'
    rack3_cntrl2 = '/html/body/div/div/div[1]/div[1]/div[4]/div[2]/input[2]'
 
    def rack_3_xpu1(self):
        print("Reseting XPU1 of Rack_3")
        rack3_xpu1 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_npu1).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_npu1).click()
        time.sleep(5)

    def rack_3_xpu2(self):
        print("Reseting XPU2 of Rack_3")
        rack5_xpu2 = '//*[@id="popup1"]/table/tbody/tr[2]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_xpu2).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_xpu2).click()
        time.sleep(5)
        
    def rack_3_xpu3(self):
        print("Reseting XPU3 of Rack_3")
        rack3_xpu3 = '//*[@id="popup1"]/table/tbody/tr[3]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_xpu3).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_xpu3).click()
        time.sleep(5)

    def rack_3_xpu4(self):
        print("Reseting XPU4 of Rack_3")
        rack3_xpu4 = '//*[@id="popup1"]/table/tbody/tr[4]/td'
        driver.find_element_by_xpath(self.rack5_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack5_xpu4).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack5_xpu4).click()
        time.sleep(5)

    def rack_3_xpu5(self):
        print("Reseting XPU5 of Rack_5")
        rack3_xpu5 = '//*[@id="popup1"]/table/tbody/tr[5]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_xpu5).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_xpu5).click()
        time.sleep(5)

    def rack_3_xpu6(self):
        print("Reseting XPU6 of Rack_3")
        rack3_xpu6 = '//*[@id="popup1"]/table/tbody/tr[6]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_xpu6).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_xpu6).click()
        time.sleep(5)

    def rack_3_xpu7(self):
        print("Reseting XPU7 of Rack_3")
        rack3_xpu7 = '//*[@id="popup1"]/table/tbody/tr[7]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_xpu7).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_xpu7).click()
        time.sleep(5)

    def rack_3_xpu8(self):
        print("Reseting XPU8 of Rack_3")
        rack3_xpu8 = '//*[@id="popup1"]/table/tbody/tr[8]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_xpu8).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_xpu8).click()
        time.sleep(5)

    def rack_3_xpu9(self):
        print("Reseting XPU9 of Rack_3")
        rack3_xpu9 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_xpu9).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_xpu9).click()
        time.sleep(5)
        
    def rack_3_riom10(self):
        print("Reseting RIOM10 of Rack_3")
        rack3_riom10 =  '//*[@id="popup1"]/table/tbody/tr[2]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_riom10).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_riom10).click()
        time.sleep(5)

    def rack_3_riom11(self):
        print("Reseting riom11 of Rack_3")
        rack3_riom11 =  '//*[@id="popup1"]/table/tbody/tr[3]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_riom11).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_riom11).click()
        time.sleep(5)

    def rack_3_riom12(self):
        print("Reseting RIOM12 of Rack_3")
        rack3_riom12 =  '//*[@id="popup1"]/table/tbody/tr[4]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_riom12).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_riom12).click()
        time.sleep(5)
        
    def rack_3_crs13(self):
        print("Reseting CRS13 of Rack_3")
        rack3_crs13 =  '//*[@id="popup1"]/table/tbody/tr[5]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_crs13).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_crs13).click()
        time.sleep(5)

    def rack_3_crs14(self):
        print("Reseting CRS14 of Rack_3")
        rack3_crs14 =  '//*[@id="popup1"]/table/tbody/tr[6]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_crs14).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_crs14).click()
        time.sleep(5)
        
    def rack_3_crs15(self):
        print("Reseting CRS15 of Rack_3")
        rack3_xpu15 =  '//*[@id="popup1"]/table/tbody/tr[7]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_crs15).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_crs15).click()
        time.sleep(5)
        
    def rack_3_crs16(self):
        print("Reseting CRS16 of Rack_3")
        rack3_crs16 =  '//*[@id="popup1"]/table/tbody/tr[8]/td'
        driver.find_element_by_xpath(self.rack3_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack3_crs16).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack3_crs16).click()
        time.sleep(5)
        
rack3 = rack_3()

while True:
    target_num = input('''
                        <----------Provide space between two numbers--------->
                                                  1 for rack3_xpu1 
                                                  2 for rack3_xpu2 
                                                  3 for rack3_xpu3 
                                                  4 for rack3_xpu4 
                                                  5 for rack3_xpu5
                                                  6 for rack3_xpu6
                                                  7 for rack3_xpu7
                                                  8 for rack3_xpu8
                                                  9 for rack3_xpu9
                                                  10 for rack3_riom10
                                                  11 for rack3_riom11
                                                  12 for rack3_riom12
                                                  13 for rack3_crs13
                                                  14 for rack3_crs14
                                                  15 for rack3_crs15
                                                  16 for rack3_crs16
                                                  0 to exit
                                                  Enter the target_num for Rack3 ON/OFF unit : ''')

    print("The Option selected is : {} ".format(target_num))

    if(int(target_num) <= 8):
        driver.get(rack3.rack3_url_index1)
        time.sleep(4)

        if(int(target_num) == 1):
            rack3.rack_3_xpu1()
            continue
        elif(int(target_num) == 2):
            rack3.rack_3_xpu2()
            continue
        elif(int(target_num) == 3):
            rack3.rack_3_xpu3()
            continue
        elif(int(target_num) == 4):
            rack3.rack_3_xpu4()
            continue
        elif(int(target_num) == 5):
            rack3.rack_3_xpu5()
            continue
        elif(int(target_num) == 6):
            rack3.rack_3_xpu6()
            continue
        elif(int(target_num) ==7):
            rack3.rack_3_xpu7()
            continue
        elif(int(target_num) ==8):
            rack3.rack_3_xpu8()
            continue
        
    elif(int(target_num) > 8):
        driver.get(rack3.rack3_url_index2)
        time.sleep(4)
        
        if(int(target_num) == 9):
            rack3.rack_3_xpu9()
            continue
        elif(int(target_num) == 10):
            rack3.rack_3_riom10()
            continue
        elif(int(target_num) == 11):
            rack3.rack_3_riom11()
            continue
        elif(int(target_num) == 12):
            rack3.rack_3_riom12()
            continue
        elif(int(target_num) == 13):
            rack3.rack_3_crs13()
            continue
        elif(int(target_num) == 14):
            rack3.rack_3_crs14()
            continue
        elif(int(target_num) ==15):
            rack3.rack_3_crs15()
            continue
        elif(int(target_num) ==16):
            rack3.rack_3_crs16()
            continue
        
    else:
        print("Exiting Loop")
    break
driver.quit()
