# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import json
import urllib.parse
import boto3
import os

webhook_url = os.getenv("SLACK_URL")

# 送信するメッセージ内容
message = {
    "text": "AWS Lambdaからの通知です。新しいイベントが発生しました。",
    "username": "AWS Lambda Bot",  # ボットの名前
    "icon_emoji": ":aws:",  # アイコン（任意で指定可能）
}


# slack_notification
def post_slack(argStr):
    request = urllib.request.Request(
        webhook_url,
        data=json.dumps(message).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request) as response:
        res_body = response.read().decode('utf-8')
        print(f"Slackに通知しました: {res_body}")


def lambda_handler(event, context):
    try:
        if not webhook_url:
            raise ValueError("Slack Webhook URLが設定されていません")
        post_slack("test")

    except Exception as e:
        print(e)
        print('Error Slack Notification: {e}')

    return {
        "statusCode": 200,
        "body": json.dumps("Slack通知を送信しました。")
    }
