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

from base import Base

class Qzone(Base):

    LOGIN_URL = "http://i.qq.com/"

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

        username_xpath = '''//*[@id="u"]'''
        pass_xpath = '''//*[@id="p"]'''
        submit_xpath = '''//*[@id="login_button"]'''

        self.driver.switch_to_frame("login_frame")
        username_element = self.driver.find_element_by_xpath(username_xpath)

        username_element.clear()
        username_element.send_keys(self.user["username"])

        pass_element = self.driver.find_element_by_xpath(pass_xpath)
        pass_element.clear()
        pass_element.send_keys(self.user["password"])

        submit_element = self.driver.find_element_by_xpath(submit_xpath)
        submit_element.click()

        #TODO Cookie
        #self.user["cookie"] = self.driver.get_cookies()

    def post(self,meg):
        logging.warning(self.driver.current_url)
        poster_xpath = '''//*[@id="QM_Mood_Poster_Inner"]'''
        input_div_xpath = '''//*[@id="$1_content_content"]'''
        send_xpath = '''//*[@id="QM_Mood_Poster_Inner"]/div/div[4]/div[4]/a[2]'''

        poster_div = self.driver.find_element_by_xpath(poster_xpath)
        poster_div.click()

        input_element = self.driver.find_element_by_xpath(input_div_xpath)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of(input_element))
        except Exception:
            logging.info(input_element.get_attribute("class"))
            logging.error("error when wait input_element visibility.")
            return
        logging.info(input_element.get_attribute("class"))
        input_element.clear()
        input_element.send_keys("")
        input_element.send_keys(meg)


        send_element = self.driver.find_element_by_xpath(send_xpath)
        send_element.click()


    def post_with_pic(self, meg, pic):
        "not work"
        raise Exception("Not support")

