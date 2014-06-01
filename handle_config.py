#!/usr/bin/env python2

import os
import os.path
import ConfigParser
CONFIG_FILE = "userinfo.cfg"

sections = ["google", "renren", "weibo", "qzone", "facebook",
        "douban", "twitter"]
options = ["username", "password", "cookie"]

def gen_default_config():
    if os.path.isfile(CONFIG_FILE):
        os.rename(CONFIG_FILE, CONFIG_FILE + ".old")

    config_parser = ConfigParser.SafeConfigParser()
    for s in sections:
        config_parser.add_section(s)
        for o in options:
            config_parser.set(s, o, "")

    with open(CONFIG_FILE, "wb") as f:
        config_parser.write(f)

def get_config_info():
    config_parser = ConfigParser.SafeConfigParser()
    config_parser.read(CONFIG_FILE)
    info = {}
    for s in config_parser.sections():
        info[s] = {}
        for item in config_parser.items(s):
            info[s][item[0]] = item[1]

    return info


if __name__ == "__main__":

    import argparse
    arg_parser = argparse.ArgumentParser(description="handle config file")
    arg_parser.add_argument("--action",action="store", default="get",
            choices=["get", "restore"], help="restore %s or get config info." % CONFIG_FILE)
    args = arg_parser.parse_args()
    if args.action == "get":
        print get_config_info()
    else:
        gen_default_config()
        print "restore %s successfully." % CONFIG_FILE



