# -*- coding:utf8 -*-
import sys

import pymysql

reload(sys)
sys.setdefaultencoding("utf8")

class MySQL_(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user="root",
            passwd="root",
            database="yun",
            charset="utf8",
            autocommit=False,
        )
        self.cursor = self.conn.cursor()

