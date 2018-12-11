import time


# from pymysql import cursors, connect
# # 测试mysql
# # 连接数据区
# conn = connect(
#     host='127.0.0.1',
#     user='root',
#     password='123456',
#     db='guest',
#     charset='utf8mb4',
#     # cursorsclass=cursors.DictCursor
# )
# try:
#     # with conn.cursor() as cursors:
#     #     # 创建嘉宾数据
#     #     sql = """INSERT INTO sing_guest (real_name, phone, email, sign, event_id, create_time) VALUES
#     #     ("tom",18680942221, "tom@email.com", 0, 1, NOW()); """
#     #     cursors.execute(sql)
#     # # 提交事务
#     # conn.commit()
#
#     with conn.cursor() as cursors:
#         sql = "select real_name, phone, email, sign from sing_guest where phone = %s"
#         cursors.execute(sql, ('18680942221',))
#         result = cursors.fetchone()
#         print(result)
# finally:
#     conn.close()
#
# now_time = str(time.time())
# print(now_time)
# ntime = now_time.split(".")[0]
# print(ntime)
# n_time = int(ntime)
# print(n_time)

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print('11111')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)


def h():
    print(1111)
    yield 5
    print(2222)

c = h()
c.__next__()
# c.__next__()
