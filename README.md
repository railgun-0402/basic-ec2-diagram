## 概要
S3にAWS構成図をアップロードしたら、構成図通りの構築を自動化する。
本リポジトリはLambdaに実装した内容を管理する。

## 内容
- diagrams + PythonでAWS構成図を作成する
- S3にアップロードすると、Labmdaがトリガーとして実行される
  - Slack通知(開始、API実行、終了)
  - bedrock APIが実行される
  - terraform作成
  - github通知

## 構成図例


![Uploading 299de1e03645-20241019.png…]()
