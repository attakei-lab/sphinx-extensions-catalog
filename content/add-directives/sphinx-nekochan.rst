===============
sphinx-nekochan
===============

:PyPI URL: https://pypi.org/project/sphinx-nekochan
:Repository: https://github.com/takanory/sphinx-nekochan
:Document: https://sphinx-nekochan.readthedocs.io/
:Author: Takanori Suzuki
:Category:
  - ディレクティブ追加
  - ロール追加
  - コンテンツ埋め込み
  - 絵文字

ドキュメント上に可愛いネコチャンを遊ばせるための拡張。

概要
====

【ネコチャン絵文字】をSphinxドキュメント内に簡単に埋め込むためのディレクティブとロールを提供します。
この絵文字はネコチャン絵文字職人である【しまかつ】氏が公開しているもので、300以上もの可愛い絵文字を簡単な記述で扱えます。 [#]_

.. [#] 【ネコチャン絵文字】そのものについては、作者のnoteを参照してください。 https://note.com/shikamatsu

使用方法
========

インストール
------------

標準的なSphinx拡張なので、インストールに特別な工夫は必要ありません。

.. code::

    pip install sphinx-nekochan

設定等
------

``conf.py`` 上での設定についても、 ``extensions`` に追加するだけで問題ありません。

.. code-block:: python

    extensions = [
        "sphinx_nekochan",
    ]

書き方
------

``extensions`` へ登録すると、 ``nekochan`` というディレクティブとロールの両方が使用可能になります。
それぞれの形式で引数に相当する部分に表示したい絵文字のコードを記載することで、ビルド時にネコチャン絵文字に変換されます。
使用可能な文字コードが非常に多いので、ドキュメントにある "List of Nekochan emoji"のページ [#]_ を参照してください。

.. [#] https://sphinx-nekochan.readthedocs.io/nekochan_emojis.html

どちらの形式も「高さを変える」「見た目を回転等させる」「alt属性を付ける」と言ったことが可能です。
基本的に、文中に表示させたいときはロール形式を、1コマ形式のように強調させたいときはディレクティブ形式を使うとよいでしょう。

.. code-block:: rst

    .. ロール形式での例

    本書を購入していただき、ありがとうございます :nekochan:`dai-kansha-nya`

.. code-block:: rst

    .. ディレクティブ形式での例（1ブロック表示をしたいので大きくする）

    .. nekochan:: dancing-nya
        :alt: リリース完了の舞！
        :height: 128px

寸評
====

ロールの形式でも使用可能なこともあり、様々な箇所への挿入が可能です。
実際にドキュメントサイトでは、目次やヘッダー行の末尾にことごとくネコチャン絵文字が散りばめられており、
よく見るドキュメントとは一風変わった雰囲気を演出するのにも役立ちます。

しまかつ氏からはきちんと許諾を取っているため、「ネコチャン絵文字のおやくそく [#]_ 」から外れない限りは安心して自由に使えます。

.. [#] https://note.com/shikamatsu/n/n8818bb5ebea1
