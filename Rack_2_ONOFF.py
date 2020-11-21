from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Python37\Scripts\chromedriver.exe')

class rack_2:
    rack2_url_index1 = 'http://10.107.74.90/index1.htm'
    rack2_url_index2 = 'http://10.107.74.90/index2.htm'
    rack2_cntrl_out = '//*[@id="control1"]'
    rack2_cntrl2 = '/html/body/div/div/div[1]/div[1]/div[4]/div[2]/input[2]'
 
    def rack_2_npu1(self):
        print("Reseting NPU1 of Rack_2")
        rack2_npu1 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_npu1).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_npu1).click()
        time.sleep(5)

    def rack_2_npu2(self):
        print("Reseting NPU2 of Rack_2")
        rack2_npu2 = '//*[@id="popup1"]/table/tbody/tr[2]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_npu2).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_npu2).click()
        time.sleep(5)
        
    def rack_2_npu3(self):
        print("Reseting NPU3 of Rack_2")
        rack2_npu3 = '//*[@id="popup1"]/table/tbody/tr[3]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_npu3).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_npu3).click()
        time.sleep(5)

    def rack_2_tcu4(self):
        print("Reseting TCU4 of Rack_2")
        rack2_tcu4 = '//*[@id="popup1"]/table/tbody/tr[4]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_tcu4).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_tcu4).click()
        time.sleep(5)

    def rack_2_tcu5(self):
        print("Reseting TCU5 of Rack_2")
        rack2_tcu5 = '//*[@id="popup1"]/table/tbody/tr[5]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_tcu5).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_tcu5).click()
        time.sleep(5)

    def rack_2_npu6(self):
        print("Reseting NPU6 of Rack_2")
        rack2_npu6 = '//*[@id="popup1"]/table/tbody/tr[6]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_npu6).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_npu6).click()
        time.sleep(5)

    def rack_2_npu7(self):
        print("Reseting NPU7 of Rack_2")
        rack2_npu7 = '//*[@id="popup1"]/table/tbody/tr[7]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_npu7).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_npu7).click()
        time.sleep(5)

    def rack_2_npu8(self):
        print("Reseting NPU8 of Rack_2")
        rack2_npu8 = '//*[@id="popup1"]/table/tbody/tr[8]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_npu8).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_npu8).click()
        time.sleep(5)

    def rack_2_tcu9(self):
        print("Reseting TCU9 of Rack_2")
        rack2_tcu9 = '//*[@id="popup1"]/table/tbody/tr[1]/td'
        driver.find_element_by_xpath(self.rack2_cntrl_out).click()
        time.sleep(2)
        driver.find_element_by_xpath(rack2_tcu9).click()
        time.sleep(5)
        driver.find_element_by_xpath(rack2_tcu9).click()
        time.sleep(5)

rack2 = rack_2()
    
while True:
    target_num = input('''
                                <----------Provide space between two numbers--------->
                                                          1 for rack2_npu1 
                                                          2 for rack2_npu2 
                                                          3 for rack2_npu3 
                                                          4 for rack2_tcu4 
                                                          5 for rack2_tcu5
                                                          6 for rack2_npu6
                                                          7 for rack2_npu7
                                                          8 for rack2_npu8
                                                          9 for rack2_tcu9
                                                          0 to exit
                                                          Enter the target_num for Rack2 ON/OFF unit : ''')

    print("The Option selected is : {} ".format(target_num))

    if(int(target_num) < 8):
        driver.get(rack2.rack2_url_index1)
        time.sleep(4)
                
        if(int(target_num) == 1):
            rack2.rack_2_npu1()
            continue
        elif(int(target_num) == 2):
            rack2.rack_2_npu2()
            continue
        elif(int(target_num) == 3):
            rack2.rack_2_npu3()
            continue
        elif(int(target_num) == 4):
            rack2.rack_2_tcu4()
            continue
        elif(int(target_num) == 5):
            rack2.rack_2_tcu5()
            continue
        elif(int(target_num) == 6):
            rack2.rack_2_npu6()
            continue
        elif(int(target_num) ==7):
            rack2.rack_2_npu7()
            continue
        elif(int(target_num) ==8):
            rack2.rack_2_npu8()
            continue
                
    elif(int(target_num) > 8):
        driver.get(rack2.rack2_url_index2)
        time.sleep(4)
        if(int(target_num) ==9):
            rack2.rack_2_tcu9()
            continue
    else:
        print("Exiting Loop")
    break
driver.quit()
