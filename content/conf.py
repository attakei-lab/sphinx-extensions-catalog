# -- Project information
project = "Sphinx拡張 ミニカタログ"
copyright = "2025, Kazuya Takei"
author = "Kazuya Takei"
release = "0.0.0"
release = "〜Sphinxユーザーによる、Sphinx拡張コレクションノート……のサンプル版〜"
release = "〜サンプル版〜"

# -- General configuration
extensions = []  # type: ignore[var-annotated]
templates_path = ["_templates"]
language = "ja"

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

latex_elements = {
    "releasename": " ",
}
