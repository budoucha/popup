# 概要
<blockquote class="twitter-video" data-lang="ja"><p lang="ja" dir="ltr">万が一スタバに行く事になってしまった時用のｶﾀｶﾀ…ﾀｰﾝ!して周囲を威嚇するやつできたー！<a href="https://t.co/MyIKngQQuo">https://t.co/MyIKngQQuo</a> <a href="https://t.co/7YJ8Ayrw4Y">pic.twitter.com/7YJ8Ayrw4Y</a></p>&mdash; ぶどう茶 (@budoucha) <a href="https://twitter.com/budoucha/status/829644496715476992">2017年2月9日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
スタバでドヤ顔する奴

# 動作条件
Windows, OpenCV3, Python3, numpy

多分上記以外では動かないと思います

(WindowsはWin32APIを画面サイズ取得に使ってるだけなので当該箇所だけ別の方法で値を渡すように変更すれば削れると思います)

# 使用方法
pythonスクリプトを実行すると始まります。

ウィンドウがポップアップするので適当なキーを押下すると

表示の「処理中」が「済」になって消えます。
これが延々続きます。

## オートモード
Ctrl+Aを押下するとオートモードに入ります。

キーを打つのに飽きてきたら勝手に生成しては消滅していくウィンドウを眺めでもしていて下さい・ω・

もう一度押下すると元に戻ります。

## 終了方法
Ctrl+C、または Esccapeキーを押下すると終了します。

オートモード中はキー入力を受け付けない時間があるため若干長押し気味にした方がいいです。

# 課題
- 何か背景に文字がバーって流れるようにしたい
- 画像表示するためだけにOpenCV使うの頭悪い気がするのでもっと頭良い方法あったら知りたい
- ウィンドウを半透明にしたい
- 若干遅いのを何とかしたい
- 画面寂しいので2,3ウィンドウくらい同時に出したい
- 画面解像度に応じてサイズ変えるとか