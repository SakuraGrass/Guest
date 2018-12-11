import time
import turtle
import random
import math


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
#
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             print('11111')
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)
#
#
# def h():
#     print(1111)
#     yield 5
#     print(2222)
#
# c = h()
# c.__next__()
# c.__next__()

def tree(n, l):
    p = turtle
    turtle.pd()
    t = math.cos(math.radians(turtle.heading() + 45)) / 8 + 0.25
    p.pencolor(t, t, t)
    p.pensize(n / 3)
    p.forward(l)
    if n > 0:
        b = random.random() * 15 + 10
        c = random.random() * 15 + 10
        d = l * (random.random() * 0.25 + 0.7)
        p.right(b)
        tree(n - 1, d)
        p.left(b + c)
        tree(n - 1, d)
        p.right(c)
    else:
        p.right(90)
        n = math.cos(math.radians(turtle.heading() - 45)) / 4 + 0.5
        p.pencolor(n, n * 0.8, n * 0.8)
        p.circle(3)
        p.left(90)
        if random.random() > 0.7:
            p.pu()
            t = turtle.heading()
            print(t)
            an = -40 + random.random() * 40
            turtle.setheading(an)
            dis = int(800 * random.random() * 0.5 + 400 * random.random() * 0.3 + 200 * random.random() * 0.2)
            p.forward(dis)
            p.setheading(t)

            p.pd()
            p.right(90)
            n = math.cos(math.radians(p.heading() - 45)) / 4 + 0.5
            p.pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
            p.circle(2)
            p.left(90)
            p.pu()

            ts = turtle.heading()
            p.setheading(an)
            p.backward(dis)
            p.setheading(ts)
    p.pu()
    p.backward(l)


turtle.bgcolor(0.5, 0.5, 0.5)
turtle.ht()
turtle.speed(0)
# turtle.tracer(0, 0)
turtle.pu()
turtle.backward(100)
turtle.left(90)
turtle.pu()
turtle.backward(300)
tree(12, 100)
turtle.done()
