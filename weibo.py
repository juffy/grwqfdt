#!/usr/bin/env python2
#!---coding:utf-8---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import logging

from base import Base, initPhantomjs

class Weibo(Base):

    INDEX_URL = "http://weibo.com"
    LOGIN_URL = "http://weibo.com/login.php"

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
        print self.LOGIN_URL
        self.driver.get(self.LOGIN_URL)
        print self.driver.current_url

        username_xpath = '''//*[@id="pl_login_form"]/div[1]/div/input'''
        pass_xpath = '''//*[@id="pl_login_form"]/div[2]/div/input'''
        savestate_xpath = '''//*[@id="login_form_savestate"]'''
        submit_xpath = '''//*[@id="pl_login_form"]/div[6]/div[1]/a'''

        username_element = self.driver.find_element_by_xpath(username_xpath)

        username_element.send_keys(self.user["username"])

        pass_element = self.driver.find_element_by_xpath(pass_xpath)
        pass_element.send_keys(self.user["password"])

        savestate_element = self.driver.find_element_by_xpath(savestate_xpath)
        #print savestate_element.is_selected()

        submit_element = self.driver.find_element_by_xpath(submit_xpath)
        submit_element.click()

        #TODO handle cookie
        #self.user["cookie"] = self.driver.get_cookies()
        logging.debug(self.driver.current_url)

    def post(self,meg):
        self.driver.get(self.INDEX_URL)
        input_xpath = '''//*[@id="pl_content_publisherTop"]/div/div[2]/textarea'''
        send_xpath = '''//*[@id="pl_content_publisherTop"]/div/div[3]/div[1]/a'''
        input_element = self.driver.find_element_by_xpath(input_xpath)
        input_element.clear()
        input_element.click()
        input_element.send_keys("")
        input_element.send_keys(meg)


        send_element = self.driver.find_element_by_xpath(send_xpath)
        logging.warning(send_element.get_attribute("class"))
        send_element.click()


    def post_with_pic(self, meg, pic):
        "not work"
        raise Exception("Not support")
        image_button_xpath = '''//*[@id="pl_content_publisherTop"]/div/div[3]/div[2]/span/a[2]'''
        image_button = self.driver.find_element_by_xpath(image_button_xpath)
        image_button.click()
        image_upload_class = "layer_send_pic_v2"
        image_upload_element = self.driver.find_element_by_class_name(image_upload_class)
        image_upload_element.click()

