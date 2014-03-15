
#!/usr/bin/env python2
#!---coding:utf-8---
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import logging

from base import Base, initPhantomjs

class Renren(Base):

    LOGIN_URL = "http://www.renren.com/SysHome.do"

    def __init__(self, user, driver):

        self.driver = driver
        self.user = user

    def login(self):
        cookie = self.user["cookie"]
        if cookie:
            self.driver.add_cookie(cookie)
            self.driver.get(self.LOGIN_URL)
            logging.debug(self.driver.current_url)
            return
        self.driver.get(self.LOGIN_URL)
        logging.warning(self.driver.current_url)

        username_xpath = '''//*[@id="email"]'''
        pass_xpath = '''//*[@id="password"]'''
        savestate_xpath = '''//*[@id="autoLogin"]'''
        submit_xpath = '''//*[@id="login"]'''

        username_element = self.driver.find_element_by_xpath(username_xpath)

        username_element.send_keys(self.user["username"])

        pass_element = self.driver.find_element_by_xpath(pass_xpath)
        pass_element.send_keys(self.user["password"])

        savestate_element = self.driver.find_element_by_xpath(savestate_xpath)
        savestate_element.click()
        logging.warning(savestate_element.is_selected())

        submit_element = self.driver.find_element_by_xpath(submit_xpath)
        submit_element.click()

        #TODO Cookie
        #self.user["cookie"] = self.driver.get_cookies()

    def post(self,meg):
        logging.warning(self.driver.current_url)
        input_xpath = '''//*[@id="global-publisher-status"]/section/div/div/div[1]/div[1]/textarea'''
        send_xpath = '''//*[@id="global-publisher-status"]/section/div/div/div[3]/div[1]/input'''

        input_element = self.driver.find_element_by_xpath(input_xpath)
        input_element.clear()
        input_element.click()
        input_element.send_keys("")
        input_element.send_keys(meg)


        send_element = self.driver.find_element_by_xpath(send_xpath)
        send_element.click()


    def post_with_pic(self, meg, pic):

        image_button_xpath = '''//*[@id="global-publisher-status"]/section/div/div/div[1]/dl/dd[2]'''
        image_button = self.driver.find_element_by_xpath(image_button_xpath)
        image_button.click()
        image_input_xpath = '''//*[@id="global-publisher-photo"]/section/div[1]/section[2]/div/input[1]'''
        image_input = self.driver.find_element_by_xpath(image_input_xpath)

        image_input.send_keys("/home/junfeng7/virtualenvs/grwqfdt/grwqfdt/error.png")

    def close(self):
        self.driver.quit()
