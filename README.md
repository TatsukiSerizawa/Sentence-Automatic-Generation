# Sentence automatic generation

Blogをデータベースとして文章の自動生成に挑戦する．また，マルコフ連鎖を用いた手法と深層学習を用いた手法での結果の違いを比較する．

## Target

- ナンスのBlogをデータセットとして，ナンスっぽい文章を生成する．

## Database

- 夏川椎菜オフィシャルブログ「ナンス・アポン・ア・タイム！」

## Program

- data/: dataset
- generate_by_markov: Sentence generation using markov chain.
- generate_by_dl: Sentence generation using deep learning.