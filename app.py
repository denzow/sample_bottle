#!/usr/bin/env python
# coding:utf-8

import sqlite3
from bottle import route, run, template, request, redirect, debug

# / にアクセスしたら index関数が呼ばれる
@route("/")
def index():
    # 画面に表示されて欲しいHTMLを戻す
    return "<h1>WELCOME STAPY!</h1>"


@route("/list")
def view_list():
    # items.dbとつなぐ(なければ作られる)
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("select id,name from items order by id")
    item_list = []
    for row in c.fetchall():
        item_list.append({
            "id": row[0],
            "name": row[1]
        })
    conn.close()
    # 表示はテンプレートを戻すだけ
    return template("list_tmpl", item_list=item_list)


@route("/add", method=["GET", "POST"])
def add_item():
    if request.method == "POST":
        # POSTアクセスならDBに登録する
        # フォームから入力されたアイテム名の取得(Python2ならrequest.POST.getunicodeを使う)
        item_name = request.POST.getunicode("item_name")
        conn = sqlite3.connect('items.db')
        c = conn.cursor()
        # 現在の最大ID取得(fetchoneの戻り値はタプル)
        new_id = c.execute("select max(id) + 1 from items").fetchone()[0]
        c.execute("insert into items values(?,?)", (new_id, item_name))
        conn.commit()
        conn.close()
        return "SUCCESS"
    else:
        # GETアクセスならフォーム表示
        return template("add_tmpl")

# /del/100 -> item_id = 100
# /del/one -> HTTPError 404
@route("/del/<item_id:int>")
def del_item(item_id):
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    # 指定されたitem_idを元にDBデータを削除
    c.execute("delete from items where id=?", (item_id,))
    conn.commit()
    conn.close()
    # 処理終了後に一覧画面に戻す
    return redirect("/list")


# サーバを起動
debug(True)
run(reloader=True, port=9999)
