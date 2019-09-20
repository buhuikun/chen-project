import numpy as np

filename = './douban.csv'

data_array = np.loadtxt(filename,
                        delimiter=',',
                        skiprows=1,
                        dtype=str,
                        usecols=(0,1),
                        encoding='utf8'
                        )

# print(data_array)
s = data_array[:, 1]
score = s.astype(np.float64)
print('电影平均分：', np.mean(score))
score_lis = s.tolist()

title_arr = data_array[:, 0]

# print('电影最高分：', np.max(score))
# print('电影9分以上：', np.where(score>8, score, 1))
print('=='*100)
# 布尔索引
bool_arry = score == np.max(score)
print('评分最高的电影：', data_array[bool_arry])
print('=='*100)
bool_arry_8 = score >= 8
print('评分高于8分的电影：', data_array[bool_arry_8])

