# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-27 20:52:18
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-28 17:02:46
# brief: 如何通过pandas写csv数据到数据库
# ref:https://blog.softhints.com/python-read-validate-and-import-csv-json-file-to-mysql/#opencsv
import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

# read CSV file
column_names = ['person','year', 'company']
'''
df = pd.read_csv('test.csv', header = None, names = column_names)
print(df)
print("-----------------------")
'''
df = pd.read_csv('test.csv', header = 0)
print(df)


engine = create_engine('mysql://root:password@localhost/test')
with engine.connect() as conn, conn.begin():
    df.to_sql('csv', conn, if_exists='append', index=False)