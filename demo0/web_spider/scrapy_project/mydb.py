import pymysql

import redis
import json


# 从redis导入到MySQL
def process_item():
    # 创建redis连接、
    rediscli = redis.Redis(host='127.0.0.1', port='6379', db=0)

    # 创建MySQL连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, db='db_spider', user='root', password='root')
    cur = conn.cursor()
    for i in range(rediscli.llen('lianjia2:items')):
        source, data = rediscli.blpop('lianjia2:items')
        # print('data',data)
        item = json.loads(data)
        # print('item:', item)
        # items = [item['title'], item['number'], item['url'], item['content'], item['author'], item['pub_date']]
        # print(items)
        items = [item['title'], item['total'], item['price'], item['hx'], item['area'], item['number']]
        sql = 'insert into t_lianjia2 values (0, %s, %s, %s, %s, %s, %s)'
        cur.execute(sql, items)
        conn.commit()

    cur.close()
    conn.close()


        # except Exception as e:
        #     print(e)

if __name__ == '__main__':
    process_item()




