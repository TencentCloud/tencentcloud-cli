**Example 1: 获取通知内容配置列表。**

获取通知内容配置列表。

Input: 

```
tccli cls DescribeNoticeContents --cli-unfold-argument  \
    --Filters.0.Key name \
    --Filters.0.Values notice-name \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NoticeContents": [
            {
                "NoticeContentId": "noticetemplate-d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1",
                "Name": "notice-name",
                "Type": 0,
                "NoticeContents": [
                    {
                        "Type": "Sms",
                        "TriggerContent": {
                            "Title": "title",
                            "Content": "this is content",
                            "Headers": []
                        },
                        "RecoveryContent": {
                            "Title": "title",
                            "Content": "this is content",
                            "Headers": [
                                "Content-Type:application/json"
                            ]
                        }
                    }
                ],
                "Flag": 0,
                "Uin": 100001,
                "SubUin": 100001,
                "CreateTime": 1693213128,
                "UpdateTime": 1693213128
            }
        ],
        "TotalCount": 1,
        "RequestId": "d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1"
    }
}
```

