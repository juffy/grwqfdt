#!/usr/bin/env python2
#!---coding:utf-8---

import argparse
import time
import logging
from selenium import webdriver

from base import initPhantomjs
from handle_config import get_config_info


from weibo import Weibo
from renren import Renren
from qzone import Qzone
from douban import Douban
from twitter import Twitter

logging.basicConfig(level="INFO")
userinfo = get_config_info()


c_dict = {'w':Weibo,
        'r':Renren,
        'q':Qzone,
        'd':Douban,
        't':Twitter
        }
u_dict = {'w':'weibo',
        'r':'renren',
        'q':'qzone',
        'd':'douban',
        't':'twitter'
        }


def proxy_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=/home/junfeng7/.config/chromium/Default")
    chrome_options.add_argument("--proxy-server=http://127.0.0.1:8087")
    return webdriver.Chrome(chrome_options=chrome_options)

class Proxy(object):
    def __init__(self, meg, sites, pic=None):
        self.meg = meg
        self.pic = pic
        self.sites = sites
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)


    def post(self):
        if not self.meg or len(self.meg) >= 140:
            logging.error("meg should't None, and length <= 140")
            return
        for c in self.sites:
            if c == "t":
                instance = c_dict[c](userinfo[u_dict[c]], proxy_driver())
            else:
                instance = c_dict[c](userinfo[u_dict[c]], self.driver)
            instance.login()
            instance.post(self.meg)
            time.sleep(1)
            logging.info("successfully post to %s." %(u_dict[c]))

    def post_with_pic(self):
        if not self.pic or  not os.path.isfile(self.pic):
            logging.error("pic must exists.")
            return
        for c in self.sites:
            instance = c_dict[c](userinfo[u_dict[c]], self.driver)
            instance.login()
            try:
                instance.post(self.meg, self.pic)
                time.sleep(2)
            except Exception, e:
                logging.error(e)
                continue
            logging.info("successfully post with pic to %s." %(u_dict[c]))

    def quit(self):
        logging.info("done")
        self.driver.quit()


def main():

    arg_parser = argparse.ArgumentParser(description="cli arguments")
    arg_parser.add_argument("-m",action="store", default=None, help="message you want to post")
    arg_parser.add_argument("-p",action="store", default=None, help="pic path you want to upload")
    arg_parser.add_argument("-s",action="store", default="wrqdt",help="help")
    args = arg_parser.parse_args()
    if args.m:
        args.m = args.m.decode("utf-8")
        logging.info(type(args.m))
        if args.p:
            args.p = args.p.decode("utf-8")
            proxy = Proxy(args.m, args.s)
            proxy.post_with_pic()
            proxy.quit()
        else:
            proxy = Proxy(args.m, args.s, args.p)
            proxy.post()
            proxy.quit()
    else:
        logging.error("message must exists.")



if __name__ == "__main__":
    main()
