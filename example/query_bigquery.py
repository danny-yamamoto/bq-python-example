from google.cloud import bigquery

# クライアントの初期化
client = bigquery.Client()

# 使用するデータセットIDとテーブルIDを指定
dataset_id = 'hogehoge'
table_id = 'example'
project_id = 'inunaki' # プロジェクトIDも必要に応じて指定

# クエリの実行
query = f"""
SELECT hoge
FROM `{project_id}.{dataset_id}.{table_id}`
WHERE id = '2024-02-01'
LIMIT 10
"""
query_job = client.query(query)  # APIリクエスト

# 結果の取得
for row in query_job:
    # rowの各フィールドにアクセスするにはrow["field_name"]を使用
    print(row)

