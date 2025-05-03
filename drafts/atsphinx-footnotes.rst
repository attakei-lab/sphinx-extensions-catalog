==================
atsphinx-footnotes
==================

:PyPI URL: https://pypi.org/project/atsphinx-footnotes
:Repository: https://github.com/atsphinx/footnotes
:Document: https://atsphinx.github.io/footnotes/
:Author: Kazuya Takei
:License: Apache License v2.0
:Category:
  - 構造操作
  - 脚注

ソース上の本文と脚注を近くに配置して、ドキュメントを管理しやすくする。

概要
====

.. todo:: 脚注記法についての解説をいれる。

SphinxやreStructuredTextは基本的にソースのままHTML形式へ変換します。
そのため、ページ内に【脚注】を起きたい場合は文末に脚注を書く必要があります。

しかし、ある程度の行数が出てくると、「注釈をいれるべき箇所」と「注釈本体」の距離が遠くなり管理しづらくなります。
特に ``[#]_`` という自動採番形式を利用すると、新たに脚注を書き加えるときにどこに差し込めばいいかを探すのも大変です。

この拡張を利用すると、ソース内に登場する脚注要素が、ビルドの段階で全て末尾に用意した脚注専用セクションへ集約されます。
そのため、注釈対象のすぐ下に脚注の内容を記述することが可能になります。

使用方法
========

インストール
------------

Pythonプロジェクトとしての名前は、ハイフンを挟む形式です。

.. code::

    pip install atsphinx-footnotes

設定等
------

Pythonパッケージとしては、ピリオドを使った形式になっています。

.. code:: python

    extensions = [
        "atsphinx.footnotes",
    ]

また、 ``conf.py`` 上で ``footnotes_rubric`` という項目を設定すると、集約された脚注セクションに付与する小タイトルを編集できます。

書き方
------

.. textlint-disable

一般的な脚注は、下記の通りあらかじめ文末に集約させておく必要がありました。
この例だと簡素なため分かりづらいかもしれませんが、長い文章になると「脚注を書く」ためにスクロールして行ったり来たりしないといけません。

.. textlint-enable

.. todo:: 日本語サンプルに差し替える。

.. code-block:: rst

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. [#]_

    The quick brown fox jumps over the lazy dog [#]_

    .. [#] This is first sentence of "Lorem ipusum"
    .. [#] This is one of pangram.

この拡張を使用すると、下記のように本文の途中に脚注を挟んでも、ビルド時に自動で集約してくれるようになります。

.. code-block:: rst

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. [#]_

    .. [#] This is first sentence of "Lorem ipusum"

    The quick brown fox jumps over the lazy dog [#]_

    .. [#] This is one of pangram.

寸評
====

Zennで記事を書いていたりすると、同様の仕様になっていることに気づくでしょう。 [#]_
技術記事などの類は1つの文書がそれなりのボリュームになるため、なるべく管理時も「編集時に楽」であることが望ましいです。

特に脚注を頻繁に使う場合は、この拡張があるとだいぶ楽になるのではないでしょうか。

.. [#] ただし、Zennの場合は採番までは自動で行われない。

動作上、どうしても「書いてある状態通りのビルド」とはいかなくなるので、その点だけは気をつける必要があります。
