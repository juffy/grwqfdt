#!/usr/bin/env python2
#!---coding:utf-8---

import unittest
import logging
import time

from selenium import webdriver

from base import initPhantomjs
from handle_config import get_config_info


from weibo import Weibo
from renren import Renren
from qzone import Qzone
from douban import Douban

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=~/.config/chromium/Default")
userinfo = get_config_info()

message = u"我不就多登陆了几次嘛，豆瓣你就开看验证码了，我可是都登陆成功了，也太不厚道了．"
pic = '/home/junfeng7/archlinux.jpg'

class WeiboCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.user = userinfo["weibo"]
        self.weibo = Weibo(self.user, self.driver)

    def test_login(self):
        self.weibo.login()

    def test_post(self):
        meg = message
        self.weibo.login()
        self.weibo.post(meg)

    def _post_with_pic(self):
        meg = None
        pic = None
        self.weibo.login()
        self.weibo.post_with_pic(meg, pic)


    def tearDown(self):
        #self.driver.quit()
        pass

class RenrenCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.user = userinfo["renren"]
        self.renren = Renren(self.user, self.driver)

    def test_login(self):
        self.renren.login()

    def test_post(self):
        meg = message
        self.renren.login()
        self.renren.post(meg)

    def _post_with_pic(self):
        meg = "just post a picture." + str(time.time())
        pic = "/home/junfeng7/archlinux.jpg"
        self.renren.login()
        self.renren.post_with_pic(meg, pic)


    def tearDown(self):
        #self.driver.quit()
        pass

class QzoneCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.user = userinfo["qzone"]
        self.qzone = Qzone(self.user, self.driver)


    def test_login(self):
        self.qzone.login()

    def test_post(self):
        meg = message
        self.qzone.login()
        self.qzone.post(meg)

    def _post_with_pic(self):
        meg = "just post a picture." + str(time.time())
        pic = "/home/junfeng7/archlinux.jpg"
        self.qzone.login()
        self.qzone.post_with_pic(meg, pic)


    def tearDown(self):
        #self.driver.quit()
        pass




class DoubanCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.user = userinfo["douban"]
        self.douban = Douban(self.user, self.driver)


    def test_login(self):
        self.douban.login()

    def test_post(self):
        meg = message
        self.douban.login()
        self.douban.post(meg)

    def test_post_with_pic(self):
        meg = message
        self.douban.login()
        self.douban.post_with_pic(meg, pic)


    def tearDown(self):
        #self.driver.quit()
        pass
if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    unittest.main()

