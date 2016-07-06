#!/usr/bin/env python
# coding:utf-8

import sqlite3

# items.dbとつなぐ(なければ作られる)
conn = sqlite3.connect('items.db')
c = conn.cursor()

# テーブル作成
c.execute("create table items(id, name)")

# 3行投入
c.execute("insert into items values(1,'りんご')")
c.execute("insert into items values(2,'ばなな')")
c.execute("insert into items values(3,'すいか')")

# 確定
conn.commit()

# バイバイ
conn.close()