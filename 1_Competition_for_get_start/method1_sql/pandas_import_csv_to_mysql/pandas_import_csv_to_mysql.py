# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-27 21:09:51
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-27 21:31:36

## 想要把tianchi_fresh_comp_train_user.csv(2千万条记录）写到mysql中，内存爆掉！

import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

# read CSV file
'''
column_names = ['person','year', 'company']
df = pd.read_csv('test.csv', header = None, names = column_names)
print(df)
print("-----------------------")
'''
df = pd.read_csv(r'..\fresh_comp_offline\tianchi_fresh_comp_train_user.csv', header = 0)
print(df)


engine = create_engine('mysql://root:password@localhost/test')
'''
with engine.connect() as conn, conn.begin():
    df.to_sql('tianchi1_train_item', conn, if_exists='append', index=False)
'''
with engine.connect() as conn, conn.begin():
    df.to_sql('tianchi1_train_user', conn, if_exists='append', index=False)