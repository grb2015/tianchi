import pandas as pd
import numpy as np

#ref : https://www.jianshu.com/p/36df85802f8d
## 比赛数据(tianchi_fresh_comp_train_item.csv)下载(需要先参赛):
#https://tianchi.aliyun.com/competition/information.htm?spm=5176.100067.5678.2.a688153cxNbRMf&raceId=231522
# pandas读取商品子集（P）
train_item=pd.read_csv('fresh_comp_offline/tianchi_fresh_comp_train_item.csv')
# 查看商品子集数据数量
print("begin")
count = train_item['item_id'].count()
print(count)
# 查看前10条商品子集数据
print(train_item.head(10))


print("----info of D-------")
# pandas读取用户商品交互数据（D）
train_user=pd.read_csv('fresh_comp_offline/tianchi_fresh_comp_train_user.csv')
# 查看用户商品交互数据数量
print(train_user['item_id'].count())
# 查看前10条商品子集数据
print(train_user.head(10))


# 查看每一列的异常值
print(train_user.apply(lambda x: sum(x.isnull())))

# 根据用户的心理行为，前一天的购物车商品很有可能第二天就被购买，
# 所以我们直接提交12月18号一天的购物车（跟商品子集交）

# 首先查看日期和行为数据
print(train_user['time'].value_counts())
print(train_user['behavior_type'].value_counts())

print("---behavior == 3-------")
# 筛选出behavior_type==3，即加入购物车数据 
train_user=train_user[train_user["behavior_type"]==3]  
print(train_user['behavior_type'].value_counts())

# 筛选出12月18号一天的数据
print("---data = 12 18 ------")
import re
regex=re.compile(r'^2014-12-18+ \d+$')
def date(column):
    if re.match(regex,column['time']):
        date,hour=column['time'].split(' ')
        return date
    else:
        return 'null'
train_user['time']=train_user.apply(date,axis=1)

train_user=train_user[(train_user['time'] =='2014-12-18')]
print(train_user.head(10))

# 删除掉多余项
train_user=train_user.drop(['user_geohash'],axis=1)
train_user=train_user.drop(['item_category'],axis=1)
train_user=train_user.drop(['behavior_type'],axis=1)
train_user=train_user.drop(['time'],axis=1)
print(train_user)
# 查看结果数据集
print(train_user['item_id'].count())
# 生成sample_submission.csv文件，保存
train_user.to_csv('sample_submission.csv',index=False)

'''
作者：Haraway
链接：https://www.jianshu.com/p/36df85802f8d
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
'''