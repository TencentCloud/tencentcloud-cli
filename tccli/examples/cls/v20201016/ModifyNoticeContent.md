**Example 1: 修改通知内容配置**

修改通知内容配置

Input: 

```
tccli cls ModifyNoticeContent --cli-unfold-argument  \
    --NoticeContentId noticetemplate-d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1 \
    --Name this is name \
    --Type 1 \
    --NoticeContents.0.Type Http \
    --NoticeContents.0.TriggerContent.Title this is title \
    --NoticeContents.0.TriggerContent.Content this is content \
    --NoticeContents.0.TriggerContent.Headers Content-Type:application/json \
    --NoticeContents.0.RecoveryContent.Title this is title \
    --NoticeContents.0.RecoveryContent.Content this is content \
    --NoticeContents.0.RecoveryContent.Headers Content-Type:application/json
```

Output: 
```
{
    "Response": {
        "RequestId": "d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1"
    }
}
```

