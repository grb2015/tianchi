此文件夹介绍了如何用pandans导入csv到mysql，对于2千万数据内存会爆，本题没有采用
bg added 20191109 即使用了chunksize也会内存爆掉
    df.to_sql('tianchi1_train_user', conn, if_exists='append', index=False,chunksize=2000)
