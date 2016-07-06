<h1>アイテム一覧</h1>
<a href='/add' >新規作成</a>
<table border="1">
%for item in item_list:
  <tr>
    <td>{{item["id"]}}</td>
    <td>{{item["name"]}}</td>
    <td><a href="/del/{{item['id']}}">削除</a></td>
  </tr>
%end
</table>