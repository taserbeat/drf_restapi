# drf_restapi

React と連携する用のバックエンド API

# 実行手順

1. プロジェクトのセットアップ

```bash
bash setup.sh
```

2. データベースのマイグレーションを実行する

\*標準で sqlite3 のデータベースでマイグレーションが行われる。

```bash
pipenv run manage migrate
```

3. admin ユーザーを作成する (任意)

```bash
pipenv run manage createsuperuser
```

| 項目             | 必須 |
| ---------------- | ---- |
| ユーザー名       | ✅   |
| E メールアドレス |      |
| パスワード       | ✅   |

4. ローカルサーバーを起動する

```bash
pipenv run start
```
