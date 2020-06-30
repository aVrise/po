# -*- coding: utf-8 -*-

import random

caidan = ["蒸蛋", "木须肉", "青椒土豆丝", "酸辣土豆丝", "豆瓣酱土豆片", "咖喱土豆", "平菇",
          "杏鲍菇", "蒜苔肉丝", "蒜黄炒蛋", "韭菜鸡蛋", "炒绿豆芽", "土豆炖豆角", "芹菜肉丝", "西兰花"]

menu = {}
menu["蒸蛋"] = "鸡蛋三个，0.75勺盐，0.5勺味素，水若干"
menu["木须肉"] = "鸡蛋两个，木耳100g"
menu["青椒土豆丝"] = "土豆800g,青椒50g"
menu["酸辣土豆丝"] = "土豆900g"
menu["豆瓣酱土豆片"] = "土豆600g"
menu["咖喱土豆"] = "土豆600g"
menu["土豆泥"] = "土豆600g"
menu["平菇"] = "平菇500g"
menu["杏鲍菇"] = "杏鲍菇500g"
menu["蒜苔肉丝"] = "蒜苔500g，猪肉100g"
menu["蒜黄炒蛋"] = "蒜黄500g"
menu["韭菜鸡蛋"] = "韭菜500g"
menu["炒绿豆芽"] = "豆芽500g"
menu["土豆炖豆角"] = "土豆200g，豆角200g"
menu["土豆炖茄子"] = "土豆200g，茄子200g"
menu["地三鲜"] = "土豆200g，茄子200g，青椒50g"
menu["芹菜肉丝"] = "芹菜400g, 鸡胸肉100g，油10+5g"
menu["西兰花"] = "西兰花500g，胡萝卜若干"


caidan = caidan + caidan

for i in ['周一', '周二', '周三', '周四']:
    a1 = random.choice(caidan)
    caidan.remove(a1)
    a2 = random.choice(caidan)
    while a1 == a2:
        a2 = random.choice(caidan)
    caidan.remove(a2)
    print
    print i
    print a1, ':', menu[a1]
    print a2, ':', menu[a2]
