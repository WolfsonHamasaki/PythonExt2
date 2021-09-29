import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエurlopenントリーから記事を入手して、ランダムに1件返却します."""
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        #resの中に、url+code+Content-Typeが格納される。
        html = res.read().decode("utf-8")
        #readメソッドで読み込みを行い、さらにutf-8形式で格納する。
    soup = BeautifulSoup(html, "htmal.parser")
    items = soup.select("item")
    shuffle(items)
    item = items[0]
    print(item)
    return json.dumps({
        "content" : item.find("title").string,
        "link": item.get('rdf:about') 
    })
 


@app.route("/api/xxxx")
def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)
