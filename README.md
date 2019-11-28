# tianchi
Practice of data  ming in  tianchi and kaggle

#1_Competition_for_get_start    天池离线赛:淘宝购买预测  https://tianchi.aliyun.com/competition/entrance/231522/information

学习笔记：
问题1 ： pandas读取大数据的csv内存错误
在YuEbao/中  # user_balance = pd.read_csv('user_balance_table.csv', parse_dates = ['report_date'])出错
解决方法：使用dask包
# Dataframes implement the Pandas API
import dask.dataframe as dd
df = dd.read_csv('s3://.../2018-*-*.csv')
Ref : https://stackoverflow.com/questions/25962114/how-to-read-a-6-gb-csv-file-with-pandas
