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
        "RequestId": "cd402dd9-a3aa-47c3-a5c0-5789d1f8875b",
        "TotalCount": 1,
        "DashboardSubscribeInfos": [
            {
                "Id": 21683,
                "Name": "订阅任务-2025-08-15_09:59",
                "DashboardId": "dashboard-522a5609-1f41-4b11-8086-5afd1d7574f5",
                "Cron": "0 0 10 * * ?",
                "SubscribeData": {
                    "DashboardTime": [
                        "now-15m",
                        "now"
                    ],
                    "TemplateVariables": null,
                    "NoticeModes": [
                        {
                            "ReceiverType": "Uin",
                            "Values": [
                                "10300000",
                                "10200000"
                            ],
                            "ReceiverChannels": [
                                "Email"
                            ],
                            "Url": ""
                        }
                    ],
                    "Timezone": "Asia/Shanghai",
                    "SubscribeLanguage": "zh",
                    "JumpDomain": "https://console.cloud.tencent.com",
                    "JumpUrl": ""
                },
                "Uin": 100001127589,
                "SubUin": 100012969012,
                "CreateTime": "2025-08-15 10:29:10",
                "UpdateTime": "2025-08-15 10:31:24",
                "LastTime": "",
                "LastStatus": "invalid"
            }
        ]
    }
}
```

