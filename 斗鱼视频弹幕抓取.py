import json
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import logging



class DouYu:
    def __init__(self):

        self.start_url = None
        self.title = None
        self.file = None
        self.driver = None
        self.barrage_list = []
        
        

    def get_barrage_info(self, barrage):
        all_barrage = barrage.split('\n')
        print("���ڽ�ȡ��"+all_barrage[0]+"�ĵ�Ļ\n")
        for i in range(len(all_barrage)):
            if i % 3 == 2:
                try:
                    self.barrage_list.append(all_barrage[i - 2]+"&&&"+all_barrage[i - 1]+'\n')
                except:
                    print("һ����Ļ��ȡδ�ɹ�")

    def run(self):
        self.start_url =  input("�����붷����Ƶ����ַ��")        
        self.driver = webdriver.Chrome()
        self.driver.get(self.start_url)
        self.title = self.driver.find_element_by_class_name('video-title').text.split('\n')
        barrage_element = self.driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='�Ƽ���Ƶ'])[1]/following::div[1]")
        barrage_element.click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        dragger = self.driver.find_element_by_id('mCSB_3_dragger_vertical')
        actions.move_to_element_with_offset(dragger, 0, 30)
        actions.perform() 
        previous_barrageCont_text = None
        barrageCont_text = None
        while True:
            barrageCont = self.driver.find_element_by_id('barrageCont')
            barrageCont_text = barrageCont.text
            if barrageCont_text == previous_barrageCont_text:
                break
            self.get_barrage_info(barrageCont_text)
            previous_barrageCont_text = barrageCont_text
            actions.click()
            actions.perform()
        self.file = open(str(self.title[0]) + " ��Ļ.txt", 'w')
        self.barrage_list = list(dict.fromkeys(self.barrage_list))
        for i in self.barrage_list:
            try:
                self.file.write(i)
            except:
                print("һ����Ļ��ȡδ�ɹ�")
        print("���")
        self.file.close()
        self.driver.quit()

if __name__=='__main__':
    douyu = DouYu()
    douyu.run()
