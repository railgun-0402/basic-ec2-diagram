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

※内容は適当

![aws構成図](https://github.com/user-attachments/assets/e6bb2b8c-9062-4b62-a9bb-2c9c60341786)
