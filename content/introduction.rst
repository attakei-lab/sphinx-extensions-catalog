========
はじめに
========

まえがき
========

今手元にあるのが見本版だとしても、読んでみようと思った方のほとんどがSphinxで実際にドキュメントなどを書いている人でしょう。

本書では、Sphinx拡張を日本でも多く公開しているエンジニアとして、また日常のドキュメントに今なおSphinxを使っている人間として、
自信が使っているものを始めとした利便性の高いSphinx拡張を紹介していきます。

.. textlint-disable

もしかしたら全く見たことがない拡張を目にするかもしれませんし、
あなたがツワモノなら「全部知ってるよ！」となるかもしれません。

.. textlint-enable

いずれにせよ、ちょっとしたミニ百科事典のつもりでお付き合いください。

まえがき（初見向け）
====================

「Sphinxというツールはほとんど聞いたことないけど手にとってみた」という方、ありがとうございます。
この本は、Python製ドキュメントビルダーであるSphinxにおける拡張機能の紹介ブックとなっています。

今でこそMkDocsをはじめとしたMarkdownをベースとしたドキュメント管理が中心となっているエンジニア領域ですが、
reStructuredTextという拡張性がより高いフォーマットを採用しているこのツールは、今なお愛好家がいます。
また、Pythonの公式ドキュメントのような場所では依然として採用されており、多くのエンジニアを支える技術と言っても良いでしょう。

.. textlint-disable

そんなSphinx（reStructuredText）の特性として、「reStructuredTextの文法に則る形式で自由に拡張が出来る」
「SphinxのAPIを通じて様々なタイミングで処理を差し込むことが出来る」という【拡張の容易さ】が挙げられます。

.. textlint-enable

本書は「拡張のカタログ」という体裁で様々なSphinx拡張していきます。
「これだけのことが出来るのか」という感想を持ってもらえればそれだけで十分な収穫となります。

本書の構成について
==================

全体の構成について
------------------

これに限らず【分類】というものは、様々な思想を含んで作り出されます。
今回、この本を書いてみる際に、Sphinx拡張を下記のような観点で分類しています。

.. textlint-disable

* Sphinxの機能を拡張するのか / テーマを提供するのか
* Sphinx本体に密結合しているのか / サードパーティー製か
* ブランド的に開発されているか / 独立的な開発か

.. textlint-enable

これらを踏まえて、本書では下記のようなセクションで紹介を区切っています。

* Sphinx本体に同梱されている拡張、Sphinx本体の依存ライブラリとなっている拡張
* 特定のブランディングとして開発されているサードパーティー製の拡張（代表的なものをいくつかピックアップ）
* 個人あるいは組織が単発で開発しているサードパーティー製の拡張（便宜上、sphinxcontribで始まるものとそうでないものに分類）
* Sphinx拡張自体が主ではないが、Sphinx拡張を同梱しているPythonプロジェクト
* Sphinxテーマ

当たり前ではありますが、掲載順に関する優劣と言ったものはありません。
あくまで今回の分類上でグルーピングした結果こうなっただけという点に留意ください。

.. todo:: 事実上最後に出てくる超有名ライブラリとかをちょっとだけ名前出しすること

ライブラリごとの紹介形式について
--------------------------------

.. todo:: 紹介形式を整理したら執筆予定。

謝辞
====

.. todo:: ちゃんと書く。

最後に、ここに紹介しきれなかったものも含めて、世界中に存在するSphinx拡張エンジニアの方々に感謝を。
