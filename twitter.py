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

class Twitter(Base):

    LOGIN_URL = "https://twitter.com/login"

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
        if self.driver.current_url == "https://twitter.com/":
            return

        username_xpath = '''//*[@id="page-container"]/div[2]/div[1]/form/fieldset/div[1]/input'''
        pass_xpath = '''//*[@id="page-container"]/div[2]/div[1]/form/fieldset/div[2]/input'''
        savestate_xpath = '''//*[@id="page-container"]/div[2]/div[1]/form/div[2]/fieldset/label/input'''
        submit_xpath = '''//*[@id="page-container"]/div[2]/div[1]/form/div[2]/button'''

        username_element = self.driver.find_element_by_xpath(username_xpath)

        username_element.send_keys(self.user["username"])

        pass_element = self.driver.find_element_by_xpath(pass_xpath)
        pass_element.send_keys(self.user["password"])

        savestate_element = self.driver.find_element_by_xpath(savestate_xpath)
        if not savestate_element.is_selected():
            savestate_element.click()
        logging.info(savestate_element.is_selected())

        submit_element = self.driver.find_element_by_xpath(submit_xpath)
        submit_element.click()

        #TODO Cookie
        #self.user["cookie"] = self.driver.get_cookies()

    def post(self,meg):
        post_button_xpath = '''//*[@id="global-new-tweet-button"]'''
        input_xpath = '''//*[@id="tweet-box-global"]'''
        send_xpath = '''//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[2]/div[2]/button'''


        post_button = self.driver.find_element_by_xpath(post_button_xpath)
        post_button.click()

        input_element = self.driver.find_element_by_xpath(input_xpath)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of(input_element))
        except Exception:
            logging.info(input_element.get_attribute("class"))
            logging.error("error when wait input_element visibility.")
            return
        input_element.clear()
        input_element.send_keys("")
        input_element.send_keys(meg)

        try:
            send_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, send_xpath)))
        except Exception, e:
            print e
            logging.info(input_element.get_attribute("class"))
            logging.error("error when wait input_element visibility.")
            return
        send_element.click()

    def post_with_pic(self, meg, pic):

        image_button_xpath = ''''''
        isay_div_xpath = '''//*[@id="db-isay"]'''
        input_xpath = '''//*[@id="isay-cont"]'''
        image_input_xpath = '''//*[@id="isay-upload-inp"]'''
        send_xpath = '''//*[@id="isay-submit"]'''

        isay_div = self.driver.find_element_by_xpath(isay_div_xpath)
        isay_div.click()
        input_element = self.driver.find_element_by_xpath(input_xpath)
        input_element.clear()
        input_element.click()
        input_element.send_keys("")
        input_element.send_keys(meg)

        image_input = self.driver.find_element_by_xpath(image_input_xpath)
        image_input.send_keys(pic)


        try:
            send_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, send_xpath)))
        except Exception, e:
            print e
            logging.info(input_element.get_attribute("class"))
            logging.error("upload %s error. exceeded 10s" % pic)
            return

        send_element.click()

