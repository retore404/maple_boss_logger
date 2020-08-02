# ページ構成（案）

- ログインページ
- 各ユーザごとのトップページ
    - ボスごとに最終登録日時を表示する
    - ボスの挑戦時刻を登録する
- サインアップページ
    - ユーザーの作成

# モデル構成（案）
- ユーザー
    - Djangoの機能で足りるので，モデルとしては用意しない
- BOSS
    - カラム
        - BOSS_ID
        - BOSS_NAME
    - とりあえず正規化用に切り出すだけ？
- USER_BOSS_RELATION
    - カラム
        - USER_ID / NAME
        - BOSS_ID
        - LAST_CHALENGED
    - どのユーザがどのボスに最後に挑戦したかの関係を保持
    - USER_IDとBOSS_IDで複合PK

