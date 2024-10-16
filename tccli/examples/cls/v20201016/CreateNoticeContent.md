**Example 1: 创建通知内容信息**

创建通知内容信息

Input: 

```
tccli cls CreateNoticeContent --cli-unfold-argument  \
    --Name testEmail \
    --Type 0 \
    --NoticeContents.0.Type Email \
    --NoticeContents.0.TriggerContent.Title title \
    --NoticeContents.0.TriggerContent.Content this is content \
    --NoticeContents.0.TriggerContent.Headers Content-Type:application/json \
    --NoticeContents.0.RecoveryContent.Title title \
    --NoticeContents.0.RecoveryContent.Content this is content \
    --NoticeContents.0.RecoveryContent.Headers Content-Type:application/json
```

Output: 
```
{
    "Response": {
        "NoticeContentId": "noticetemplate-d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1",
        "RequestId": "d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1"
    }
}
```

