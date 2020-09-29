# 1. Python3のインストール

Python3をインストールしてください．

# 2. 認証資格情報の設定，取得

プログラムを実行する前に，プロジェクトの認証資格情報を設定する必要があります．:

1. [Google API Console](https://console.developers.google.com/)にアクセスし， ***<font color=#bbddff>プロジェクトを作成</font>*** する．
2. サイドバーから ***<font color=#bbddff>[ライブラリ]</font>*** ページに行き， *"YouTube"* と検索窓に入力する． ***<font color=#ff0050>YouTube Data API v3</font>*** と ***<font color=#ff0050>YouTube Analytics API</font>*** をそれぞれ有効にする．
3. サイドバーから ***<font color=#bbddff>[OAuth 同意画面]</font>*** ページに行き，アプリケーション名（ *"YouTube-API"* など）およびメールアドレスを入力後， ***<font color=#bbddff>保存</font>*** ボタンを押す．
4. サイドバーから ***<font color=#bbddff>[認証情報]</font>*** ページに行き， ***<font color=#bbddff>+認証情報を作成</font>*** を押し， ***<font color=#bbddff>OAuth クライアント ID</font>*** ボタンを押す．
5. アプリケーションの種類は ***<font color=#bbddff>デスクトップ アプリ</font>*** を選択し，名前欄に *"YouTube-API"* などと入力後，***<font color=#bbddff>作成</font>*** ボタンを押す．
6. 作成が完了したという内容のポップアップが出てきたら， ***<font color=#bbddff>OK</font>*** を押す．
7. 作成したクライアント IDの右側にあるダウンロードボタンを押し，PCに認証に必要なJSONファイルをダウンロードする．
8. サイドバーから ***<font color=#bbddff>[認証情報]</font>*** ページに行き， ***<font color=#bbddff>+認証情報を作成</font>*** を押し， ***<font color=#bbddff>API キー</font>*** ボタンを押す．
9. 生成されたAPI キーをコピーする．

# 3. 本プロジェクトのダウンロード

次に，このプロジェクトをダウンロードします．:

1. このページ右上の， ***<font color=#bbddff>Code</font>*** ボタンを押し，***<font color=#bbddff>Download ZIP</font>*** を押す．
2. ダウンロードしたZIPファイルを展開し，そのフォルダを好きなディレクトリにおく．
3. ターミナル（コマンドプロンプト）でプロジェクトのルートディレクトリに移動し，*requirements.txt* 内に示されたライブラリを以下のコマンドでインストールする．

```sh
pip3 install -r requirements.txt
```

# 4. 認証資格情報の適用

プログラムから， **2. 認証資格情報の設定，取得** で取得した認証資格情報を使用するために，コードを編集します．

1. **2. 認証資格情報の設定，取得** でダウンロードしたJSONファイルを，プロジェクトのルートディレクトリに移動する．
2. プロジェクトディレクトリ内の`main.py`を使い慣れたエディタ（VSCodeやサクラエディタやメモ帳など）で開く．
3. `main.py`内の以下の3行を書き換える．

```python
CLIENT_SECRETS_FILE = 'FILE NAME HERE!!!'
YOUTUBE_DATA_API_KEY = 'API KEY HERE!!!'
CHANNEL_ID = 'CHANNEL ID HERE!!!'
```

`FILE NAME HERE!!!`を **2. 認証資格情報の設定，取得** でダウンロードしたJSONファイルの名前にする．

`API KEY HERE!!!`を **2. 認証資格情報の設定，取得** でコピーした API キーの値にする．

`CHANNEL ID HERE!!!`を，自分のYouTubeチャンネルのIDの値にする．

# 5. 実行

ターミナル（コマンドプロンプト）でプロジェクトのルートディレクトリに移動し，以下のコマンドで，プログラムを実行してください．

```sh
python3 main.py
```

Windowsの場合は，`python3`を`python`に置き換えて実行してください．

最初の実行時には，ブラウザが開き，Googleから認証を求められるので，許可してください．

# 6. 実行結果

実行にはしばらく（数秒）時間がかかります．

実行が正常に終了すると，同ディレクトリに，`token.pickle`と`videos_report.csv`の2つの新しいファイルが生成されます．

`token.pickle`は，次回からブラウザ上でのGoogle認証を省略するために必要なファイルです．`videos_report.csv`をExcelなどで開くと，必要な情報が得られていることがわかります．