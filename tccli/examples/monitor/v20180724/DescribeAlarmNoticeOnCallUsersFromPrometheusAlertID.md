**Example 1: 通过prometheus告警分组id查询该策略的当前通知人**



Input: 

```
tccli monitor DescribeAlarmNoticeOnCallUsersFromPrometheusAlertID --cli-unfold-argument  \
    --AlertId alert-********
```

Output: 
```
{
    "Response": {
        "Notices": [
            {
                "NoticeId": "notice-********",
                "SendGroups": [
                    {
                        "ReceiverType": "GROUP",
                        "Users": [
                            {
                                "UserId": "10***37",
                                "UserName": "iv****ai"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "a983a961-d495-4332-a438-29c3c895d136"
    }
}
```

