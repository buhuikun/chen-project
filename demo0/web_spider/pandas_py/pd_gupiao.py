import pandas as pd

# 加载csv数据
data_arr = pd.read_csv('./gupiao.csv')
#print(data_arr)

# 获取股票代码
print('获取股票代码:')
print(data_arr['code'])
# 等价的方式
print(data_arr.code)
# 2、获取前五行的股票数据
print('2、获取前五行的股票数据:')
print(data_arr.head())
print(data_arr.loc[0:4,:])
print(data_arr.iloc[0:5,:])
# 3、返回第一只股票的股价
print('3、返回第一只股票的股价:')
print(data_arr.loc[0,'tradePrice'])
print(data_arr.iloc[0,2])

# 4、计算平均的股价
print('4、计算平均的股价:')
print(data_arr.tradePrice.mean())
print(data_arr['tradePrice'].mean())
# 5、计算股价大于180的公司的名称
print('5、计算股价大于180的公司的名称:')
bool_arr = data_arr['tradePrice'] > 180
print(bool_arr)
print(data_arr[bool_arr])
print(data_arr[bool_arr]['name'])
# 6、找出股价前三名的公司，降序排序
print('6、找出股价前三名的公司，降序排序:')
results = data_arr.sort_values(by='tradePrice',ascending=False)
print(results[:3])
print(results[:3].name)