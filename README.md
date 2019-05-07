# Sentence automatic generation

Blogをデータベースとして文章の自動生成に挑戦する．また，マルコフ連鎖を用いた手法と深層学習を用いた手法での結果の違いを比較する．

## Target

- ナンスのBlogをデータセットとして，ナンスっぽい文章を生成する．

## Dataset source

- 夏川椎菜オフィシャルブログ「ナンス・アポン・ア・タイム！」

## Program

- data/: dataset
- scraping.py: Get sentences from blog.
- generate_by_markov.py: Sentence generation using markov chain.
- generate_by_dl.py: Sentence generation using deep learning.

## Reference

- アメブロのブログ記事をスクレイピングで全件取得する方法: http://be-07.hatenablog.com/entry/2016/12/23/012055