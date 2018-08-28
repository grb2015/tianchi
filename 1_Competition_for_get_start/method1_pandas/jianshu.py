import pandas as pd
import numpy as np

## 关于pandas 的applay方法 其实就是把函数对表内的所有元素作用
## 参考 ： https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html

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
print("查看异常值 begin....")
print(train_user.apply(lambda x: sum(x.isnull()))) ## 这里打印是train_user表中每一列为空的数目
print("查看异常值 end ....")						   ## 比如user_id为空的有多少条?item_id为空的有多少条					

# 根据用户的心理行为，前一天的购物车商品很有可能第二天就被购买，
# 所以我们直接提交12月18号一天的购物车（跟商品子集交）

# 首先查看日期和行为数据
'''
rbguo added 这里统计的是
比如train_user['behavior_type'].value_counts() 得到：
1      21940520 # 浏览的条数
3      659437   # 加购物车的条数
2      458491
4      232579
也就是说,这里统计的behavior_type中不同值的计数求和，类似于数据透视表的计数求和
而train_user['time'].value_counts()统计的是time中不同时间的求和，得到30天中每天24个时间点的流量统计
'''
print("----- value_counts beign ...")
print(train_user['time'].value_counts())
print(train_user['behavior_type'].value_counts())
print("----- value_counts end ...")

print("---behavior == 3-------")
# 筛选出behavior_type==3，即加入购物车数据 
train_user=train_user[train_user["behavior_type"]==3]  ## 注意, train_user["behavior_type"]==3是一个判断吧
print(train_user['behavior_type'].value_counts())	   ## 所以pandas这种"切片"还是很方便，代替了sql中的一个查询

# 筛选出12月18号一天的数据
print("---data = 12 18 ------")
import re
regex=re.compile(r'^2014-12-18+ \d+$')
global i 
i = 0
def date(column):
	#print("column = \n",column) ## 打印可见这里的coulumn是每一行的数据
	if re.match(regex,column['time']):
		date,hour=column['time'].split(' ')	## 日期和时辰 比如2014-12-18 08  
		return date	## 只要日期就好了
	else:
		return 'null'
train_user['time']=train_user.apply(date,axis=1)  ## data的作用是对time列去掉时辰,只保留日期

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