from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Python37\Scripts\chromedriver.exe')

class rack_1:
    rack1_url_index1 = 'http://10.107.74.59/index1.htm'
    rack1_url_index2 = 'http://10.107.74.59/index2.htm'
    rack1_cntrl_out = '//*[@id="control1"]'
    rack1_cntrl2 = '/html/body/div/div/div[1]/div[1]/div[4]/div[2]/input[2]'
 
    def rack_1_npu1(self):
        print("Reseting NPU1 of Rack_1")
        rack1_npu1 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_npu1).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_npu1).click()
        time.sleep(5)

    def rack_1_npu2(self):
        print("Reseting NPU2 of Rack_1")
        rack1_npu2 = '//*[@id="popup1"]/table/tbody/tr[2]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_npu2).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_npu2).click()
        time.sleep(5)
        
    def rack_1_npu3(self):
        print("Reseting NPU3 of Rack_1")
        rack1_npu3 = '//*[@id="popup1"]/table/tbody/tr[3]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_npu3).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_npu3).click()
        time.sleep(5)

    def rack_1_tcu4(self):
        print("Reseting TCU4 of Rack_1")
        rack1_tcu4 = '//*[@id="popup1"]/table/tbody/tr[4]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_tcu4).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_tcu4).click()
        time.sleep(5)

    def rack_1_npu5(self):
        print("Reseting NPU5 of Rack_1")
        rack1_npu5 = '//*[@id="popup1"]/table/tbody/tr[5]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_npu5).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_npu5).click()
        time.sleep(5)

    def rack_1_npu6(self):
        print("Reseting NPU6 of Rack_1")
        rack1_npu6 = '//*[@id="popup1"]/table/tbody/tr[6]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_npu6).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_npu6).click()
        time.sleep(5)

    def rack_1_npu7(self):
        print("Reseting NPU7 of Rack_1")
        rack1_npu7 = '//*[@id="popup1"]/table/tbody/tr[7]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_npu7).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_npu7).click()
        time.sleep(5)

    def rack_1_tcu8(self):
        print("Reseting TCU8 of Rack_1")
        rack1_tcu8 = '//*[@id="popup1"]/table/tbody/tr[8]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_tcu8).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_tcu8).click()
        time.sleep(5)

    def rack_1_tcu9(self):
        print("Reseting TCU9 of Rack_4")
        rack1_tcu9 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_tcu9).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_tcu9).click()
        time.sleep(5)
        
    def rack_1_xpu10(self):
        print("Reseting XPU10 of Rack_1")
        rack1_xpu10 =  '//*[@id="popup1"]/table/tbody/tr[2]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_xpu10).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_xpu10).click()
        time.sleep(5)

    def rack_1_out11(self):
        print("Reseting OUT11 of Rack_1")
        rack1_out11 =  '//*[@id="popup1"]/table/tbody/tr[3]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_out11).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_out11).click()
        time.sleep(5)

    def rack_1_xpu12(self):
        print("Reseting XPU12 of Rack_1")
        rack1_xpu12 =  '//*[@id="popup1"]/table/tbody/tr[4]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_xpu12).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_xpu12).click()
        time.sleep(5)
        
    def rack_1_xpu13(self):
        print("Reseting XPU13 of Rack_1")
        rack1_xpu13 =  '//*[@id="popup1"]/table/tbody/tr[5]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_xpu13).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_xpu13).click()
        time.sleep(5)

    def rack_1_crs14(self):
        print("Reseting CRS14 of Rack_1")
        rack1_crs14 =  '//*[@id="popup1"]/table/tbody/tr[6]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_crs14).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_crs14).click()
        time.sleep(5)
        
    def rack_1_crs15(self):
        print("Reseting CRS15 of Rack_1")
        rack1_crs15 =  '//*[@id="popup1"]/table/tbody/tr[7]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_crs15).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_crs15).click()
        time.sleep(5)
        
    def rack_1_xpu16(self):
        print("Reseting XPU16 of Rack_1")
        rack1_xpu16 =  '//*[@id="popup1"]/table/tbody/tr[8]/td'
        driver.find_element_by_xpath(self.rack1_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack1_xpu16).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack1_xpu16).click()
        time.sleep(5)
        
rack1 = rack_1()

while True:
    target_num = input('''
                        <----------Provide space between two numbers--------->
                                                  1 for rack1_npu1 
                                                  2 for rack1_npu2 
                                                  3 for rack1_npu3 
                                                  4 for rack1_tcu4 
                                                  5 for rack1_npu5
                                                  6 for rack1_npu6
                                                  7 for rack1_npu7
                                                  8 for rack1_tcu8
                                                  9 for rack1_tcu9
                                                  10 for rack1_xpu10
                                                  11 for rack1_out11
                                                  12 for rack1_xpu12
                                                  13 for rack1_xpu13
                                                  14 for rack1_crs14
                                                  15 for rack1_crs15
                                                  16 for rack1_xpu16
                                                  0 to exit
                                                  Enter the target_num for Rack1 ON/OFF unit : ''')

    print("The Option selected is : {} ".format(target_num))

    if(int(target_num) <= 8):
        driver.get(rack1.rack1_url_index1)
        time.sleep(4)

        if(int(target_num) == 1):
            rack1.rack_1_npu1()
            continue
        elif(int(target_num) == 2):
            rack1.rack_1_npu2()
            continue
        elif(int(target_num) == 3):
            rack1.rack_1_npu3()
            continue
        elif(int(target_num) == 4):
            rack1.rack_1_tcu4()
            continue
        elif(int(target_num) == 5):
            rack1.rack_1_npu5()
            continue
        elif(int(target_num) == 6):
            rack1.rack_1_npu6()
            continue
        elif(int(target_num) ==7):
            rack1.rack_1_npu7()
            continue
        elif(int(target_num) ==8):
            rack1.rack_1_tcu8()
            continue
        
    elif(int(target_num) > 8):
        driver.get(rack1.rack1_url_index2)
        time.sleep(4)
        
        if(int(target_num) == 9):
            rack1.rack_1_tcu9()
            continue
        elif(int(target_num) == 10):
            rack1.rack_1_xpu10()
            continue
        elif(int(target_num) == 11):
            rack1.rack_1_out11()
            continue
        elif(int(target_num) == 12):
            rack1.rack_1_xpu12()
            continue
        elif(int(target_num) == 13):
            rack1.rack_1_xpu13()
            continue
        elif(int(target_num) == 14):
            rack1.rack_1_crs14()
            continue
        elif(int(target_num) ==15):
            rack1.rack_1_crs15()
            continue
        elif(int(target_num) ==16):
            rack1.rack_1_xpu16()
            continue
        
    else:
        print("Exiting Loop")
    break
driver.quit()
