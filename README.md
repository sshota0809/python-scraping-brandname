# python-scraping-brandname
folio の任意のテーマに関連する銘柄一覧を取得する web api サーバプログラム。

## Features
  * endpoint: `/brandname` にアクセスすることで銘柄一覧を取得
  * json 形式でレスポンスを返却

## Requirements
  * python (3.0.0+)
  * beautifulsoup4 (4.7.1)
  * Flask (1.0.3)

## Installation
下記手順に従って指定ディレクトリに git clone を実施してください。
``` bash
$ cd
$ git clone https://github.com/sshota0809/python-scraping-brandname
```

## Usage
下記手順に従って利用してください。

### Initial setting
必要な module のインストールを実行。
``` bash
$ pip install -r requirements.txt
```

### Execution
cloneしたディレクトリ配下で web api サーバを起動。
  * bind
    * ip: `0.0.0.0`
    * port: `8000`

``` bash
$ python3 -m main
```

endpoint: `/brandname` に parameter: `theme` を付与して `GET` リクエストを送信することで任意のテーマの銘柄が取得可能。

``` bash
$ curl http://localhost:8000/brandname?theme=kyoto
{"brandname":["任天堂","ジーエスユアサコーポレーション","村田製作所","日本電産","日本新薬","ローム","京セラ","島津製作所","オムロン","堀場製作所"],"result":{"code":1,"message":"success"}}
```

### result
api 実行結果はレスポンス内の `result: {"code", "message"}` に格納されます。

* code
  * 1: `取得成功`
  * 0: `取得失敗`
