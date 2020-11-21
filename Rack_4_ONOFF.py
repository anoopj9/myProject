from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Python37\Scripts\chromedriver.exe')

class rack_4:
    rack4_url_index1 = 'http://10.107.74.99/index1.htm'
    rack4_url_index2 = 'http://10.107.74.99/index2.htm'
    rack4_cntrl_out = '//*[@id="control1"]'
    rack4_cntrl2 = '/html/body/div/div/div[1]/div[1]/div[4]/div[2]/input[2]'
 
    def rack_4_npu1(self):
        print("Reseting NPU1 of Rack_4")
        rack4_npu1 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_npu1).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_npu1).click()
        time.sleep(5)

    def rack_4_npu2(self):
        print("Reseting NPU2 of Rack_4")
        rack4_npu2 = '//*[@id="popup1"]/table/tbody/tr[2]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_npu2).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_npu2).click()
        time.sleep(5)
        
    def rack_4_out3(self):
        print("Reseting OUT3 of Rack_4")
        rack4_out3 = '//*[@id="popup1"]/table/tbody/tr[3]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_out3).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_out3).click()
        time.sleep(5)

    def rack_4_npu4(self):
        print("Reseting NPU4 of Rack_4")
        rack4_npu4 = '//*[@id="popup1"]/table/tbody/tr[4]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_npu4).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_npu4).click()
        time.sleep(5)

    def rack_4_tcu5(self):
        print("Reseting TCU5 of Rack_4")
        rack4_tcu5 = '//*[@id="popup1"]/table/tbody/tr[5]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_tcu5).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_tcu5).click()
        time.sleep(5)

    def rack_4_npu6(self):
        print("Reseting NPU6 of Rack_4")
        rack4_npu6 = '//*[@id="popup1"]/table/tbody/tr[6]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_npu6).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_npu6).click()
        time.sleep(5)

    def rack_4_tcu7(self):
        print("Reseting TCU7 of Rack_4")
        rack4_tcu7 = '//*[@id="popup1"]/table/tbody/tr[7]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_tcu7).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_tcu7).click()
        time.sleep(5)

    def rack_4_tcu8(self):
        print("Reseting TCU8 of Rack_4")
        rack4_tcu8 = '//*[@id="popup1"]/table/tbody/tr[8]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_tcu8).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_tcu8).click()
        time.sleep(5)

    def rack_4_out9(self):
        print("Reseting OUT9 of Rack_4")
        rack4_out9 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_out9).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_out9).click()
        time.sleep(5)
        
    def rack_4_crs10(self):
        print("Reseting CRS10 of Rack_4")
        rack4_crs10 =  '//*[@id="popup1"]/table/tbody/tr[2]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_crs10).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_crs10).click()
        time.sleep(5)

    def rack_4_crs11(self):
        print("Reseting CRS11 of Rack_4")
        rack4_crs11 =  '//*[@id="popup1"]/table/tbody/tr[3]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_crs11).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_crs11).click()
        time.sleep(5)

    def rack_4_crs12(self):
        print("Reseting CRS12 of Rack_4")
        rack4_crs12 =  '//*[@id="popup1"]/table/tbody/tr[4]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_crs12).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_crs12).click()
        time.sleep(5)
        
    def rack_4_dmi13(self):
        print("Reseting DMI13 of Rack_4")
        rack4_dmi13 =  '//*[@id="popup1"]/table/tbody/tr[5]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_dmi13).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_dmi13).click()
        time.sleep(5)

    def rack_4_dmi14(self):
        print("Reseting DMI14 of Rack_4")
        rack4_dmi14 =  '//*[@id="popup1"]/table/tbody/tr[6]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_dmi14).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_dmi14).click()
        time.sleep(5)
        
    def rack_4_dmi15(self):
        print("Reseting DMI15 of Rack_4")
        rack4_dmi15 =  '//*[@id="popup1"]/table/tbody/tr[7]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_dmi15).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_dmi15).click()
        time.sleep(5)
        
    def rack_4_dmi16(self):
        print("Reseting DMI16 of Rack_4")
        rack4_dmi16 =  '//*[@id="popup1"]/table/tbody/tr[8]/td'
        driver.find_element_by_xpath(self.rack4_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack4_dmi16).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack4_dmi16).click()
        time.sleep(5)
        
rack4 = rack_4()

while True:
    target_num = input('''
                        <----------Provide space between two numbers--------->
                                                  1 for rack2_npu1 
                                                  2 for rack2_npu2 
                                                  3 for rack2_npu3 
                                                  4 for rack2_tcu4 
                                                  5 for rack2_tcu5
                                                  6 for rack2_npu6
                                                  7 for rack2_tcu7
                                                  8 for rack2_tcu8
                                                  9 for rack2_out9
                                                  10 for rack2_crs10
                                                  11 for rack2_crs11
                                                  12 for rack2_crs12
                                                  13 for rack2_dmi13
                                                  14 for rack2_dmi14
                                                  15 for rack2_dmi15
                                                  16 for rack2_dmi16
                                                  0 to exit
                                                  Enter the target_num for Rack4 ON/OFF unit : ''')

    print("The Option selected is : {} ".format(target_num))

    if(int(target_num) <= 8):
        driver.get(rack4.rack4_url_index1)
        time.sleep(4)

        if(int(target_num) == 1):
            rack4.rack_4_npu1()
            continue
        elif(int(target_num) == 2):
            rack4.rack_4_npu2()
            continue
        elif(int(target_num) == 3):
            rack4.rack_4_out3()
            continue
        elif(int(target_num) == 4):
            rack4.rack_4_npu4()
            continue
        elif(int(target_num) == 5):
            rack4.rack_4_tcu5()
            continue
        elif(int(target_num) == 6):
            rack4.rack_4_npu6()
            continue
        elif(int(target_num) ==7):
            rack4.rack_4_tcu7()
            continue
        elif(int(target_num) ==8):
            rack4.rack_4_tcu8()
            continue
        
    elif(int(target_num) > 8):
        driver.get(rack4.rack4_url_index2)
        time.sleep(4)
        
        if(int(target_num) == 9):
            rack4.rack_4_out9()
            continue
        elif(int(target_num) == 10):
            rack4.rack_4_crs10()
            continue
        elif(int(target_num) == 11):
            rack4.rack_4_crs11()
            continue
        elif(int(target_num) == 12):
            rack4.rack_4_crs12()
            continue
        elif(int(target_num) == 13):
            rack4.rack_4_dmi13()
            continue
        elif(int(target_num) == 14):
            rack4.rack_4_dmi14()
            continue
        elif(int(target_num) ==15):
            rack4.rack_4_dmi15()
            continue
        elif(int(target_num) ==16):
            rack4.rack_4_dmi16()
            continue
        
    else:
        print("Exiting Loop")
    break
driver.quit()
