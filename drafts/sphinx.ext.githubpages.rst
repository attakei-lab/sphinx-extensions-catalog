======================
sphinx.ext.githubpages
======================

:PyPI URL: https://pypi.org/project/Sphinx
:Repository: https://github.com/sphinx-doc/sphinx
:Document: https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
:Author: Sphinx GitHub Organization
:License: 2-clause BSD license
:Category:
  - ファイル追加
  - GitHub Pages

GitHub Pagesへデプロイを行う際のちょっとしたひと手間を軽減する。

概要
====

このSphinx拡張が行うことは、たった1つ「ビルドの出力先ルートに ``.nojekyll`` という空ファイルを配置する」だけです。

GitHubが1機能として提供している「静的サイトのデプロイ基盤」であるGitHub Pagesには、
Ruby製の静的サイトジェネレーターであるJekyllが採用されています。
とはいえあくまで基盤にJekyllを使っているだけであり、多くの静的サイトジェネレーターからみたら
「ビルド済み静的サイトをJekyll内でのビルドなしにデプロイする」ものと考えてもらえば良いです。

さて、Jekyll環境として動く際の制約の1つに「 ``_`` から始まるフォルダはビルド対象外となる」というものがあります。
困ったことに、SphinxでHTMLをビルドすると、「 ``_static`` に共通の静的ファイルを配置する」
「 ``_images`` にコンテンツの画像などを配置する」という動作をするため、多くのファイルがデプロイされなくなっています。

同種の現象に対する回避策として、GitHub Pagesは「ルート `` .nojekyll`` ファイルがあると、直接ファイルをデプロイする」
という動作も用意しています。
このSphinx拡張は、この直接ファイルをデプロイするためのファイルを配置することだけをやっています。

使用方法
========

インストール
------------

Sphinx本体に同梱されているため、追加のインストールは不要です。

設定等
------

Sphinx拡張の使用を ``conf.py`` 内で宣言するだけでよいです。
この拡張のみに関与する設定項目は一切ありません。

.. code:: python

    extensions = [
        "sphinx.ext.githubpages",
    ]

書き方
------

ここまでの説明にもある通り、ドキュメントソースで何かするタイプのものではないため、「書き方」と言えるものも存在しません。

寸評
====

「1つのことをシンプルに実行する」という表現が非常に似合うSphinx拡張です。
使うべきシーンがはっきりしているため、「GitHub Pagesへのデプロイ」を考えているならば何も考えずに登録しておけばよいでしょう。

当然ながら、GitHub Pagesへのデプロイをしないのであれば基本的に無用の長物です。
ビルド時間の無駄なので、わざわざ登録する必要はありません。
