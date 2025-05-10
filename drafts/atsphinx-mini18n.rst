================
atsphinx-mini18n
================

:PyPI URL: https://pypi.org/project/atsphinx-mini18n
:Repository: https://github.com/atsphinx/mini18n
:Document: https://atsphinx.github.io/mini18n/
:Author: Kazuya Takei
:License: Apache License v2.0
:Category:
  - ビルダー追加

単一ホスティング環境に、国際化対応したSphinx製HTMLをデプロイするための補助ビルダー。

概要
====

Sphinxには標準で国際化対応のための機能が備わっています。
また、補助ツールである sphinx-intl を用いることで、国際化対応に向いた "POファイル" も容易に作成できます。

一方で、「国際化対応したサイトをちゃんと多言語切り替えできるようにデプロイする」となるとちょっと考える必要があります。

.. todo:: 一般的なデプロイケースを記述する。

その補助として作られたのがこのSphinx拡張です。

拡張自体は新しいビルダーを提供するというわけではなく、HTML系のビルダーを検知したときに新しい ``mini18n-`` ビルダーを作る機能を持っています。
この ``mini18n-`` ビルダーは、内部では設定で指定された各言語版のHTMLをビルドした上で言語ごとのフォルダに格納し、
ビルド先のトップには自動遷移するJavaSriptのみをもつページを生成します。

そのため、GitHub Pagesのような単一のデプロイ先でも「複数言語によるページを持ち」「切り替えが用意」なドキュメントサイトを組み立てることができます。

使用方法
========

インストール
------------

Pythonプロジェクトとしての名前は、ハイフンを挟む形式です。

.. code::

    pip install atsphinx-mini18n

設定等
------

Pythonパッケージとしては、ピリオドを使った形式になっています。
また、 ``extensions`` だけでなく、 ``mini18n_default_language`` と ``mini18n_support_languages`` も実質的に必須の設定項目と言えるでしょう。

.. code:: python

    extensions = [
        "atsphinx.mini18n",
    ]

    # 初期状態で、ページトップのJavaScriptがどの言語へ遷移させるか
    mini18n_default_language = "en"
    # 各ドキュメント内に挿入するナビゲーションが選択可能な一覧
    mini18n_support_languages = ["en", "ja"]

また、 ``conf.py`` 上で ``footnotes_rubric`` という項目を設定すると、集約された脚注セクションに付与する小タイトルを編集できます。

書き方
------

ドキュメントのソース自体は特に何も作用しないため、普通にドキュメントを書きましょう。

寸評
====

Read the Docsを用いた多言語サイトの構築は便利ではあるものの、仕組み上の理由からどうしても言語間でのバージョン差異などを生み出しやすい構造になっています。

これを使うと複数言語サイトを一つのサイトとして生成するため、ビルドプロセス自体はイージーになることは期待できます。
