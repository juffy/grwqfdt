#!/usr/bin/env python2
#!---coding:utf-8---
import logging


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def initPhantomjs():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36"
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    #driver = webdriver.Chrome()
    driver.set_window_size(1027,768)
    return driver

class Base(object):
    LOGIN_URL = ""

    def login(self, cookie=None):
        raise NotImplementedError

    def post(self, meg):
        raise NotImplementedError

    def post_with_pic(self, meg, pic):
        raise NotImplementedError

