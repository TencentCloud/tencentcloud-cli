**Example 1: 获取仪表盘订阅列表**



Input: 

```
tccli cls DescribeDashboardSubscribes --cli-unfold-argument  \
    --Offset 10 \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DashboardSubscribeInfos": [
            {
                "Name": "每月最后一天早晨10点",
                "DashboardId": "xxx-xxxxxx-xxxxxxx-xxxxxxxx",
                "Cron": "0 0 10 L * ?",
                "SubscribeData": {
                    "DashboardTime": [
                        "2022-05-01T00:00:00.000",
                        "2022-05-31T23:59:59.999"
                    ],
                    "StyleLayout": 1,
                    "TemplateVariables": [
                        {
                            "Key": "topic_id"
                        },
                        {
                            "Key": "variable_1"
                        }
                    ],
                    "NoticeModes": [
                        {
                            "ReceiverType": "Uin",
                            "Values": [
                                "168053"
                            ],
                            "ReceiverChannels": [
                                "Sms"
                            ]
                        },
                        {
                            "ReceiverType": "Group",
                            "Values": [
                                "10721522",
                                "9553840"
                            ],
                            "ReceiverChannels": [
                                "Sms"
                            ]
                        },
                        {
                            "ReceiverType": "Email",
                            "Values": [
                                "3333@qq.com",
                                "xxx@163.com"
                            ],
                            "ReceiverChannels": []
                        }
                    ]
                }
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

