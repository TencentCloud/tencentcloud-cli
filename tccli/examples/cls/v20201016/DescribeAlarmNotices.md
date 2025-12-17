**Example 1: 获取通知渠道组列表**



Input: 

```
tccli cls DescribeAlarmNotices --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "AlarmNotices": [
            {
                "Type": "",
                "Name": "test-qywx",
                "AlarmNoticeId": "notice-5281f1d2-6275-4e56-9ec3-a1eb19d8bc2f",
                "CreateTime": "2025-08-06 15:47:00",
                "UpdateTime": "2025-08-06 15:47:00",
                "NoticeReceivers": [],
                "WebCallbacks": [],
                "Tags": [],
                "JumpDomain": "https://console.cloud.tencent.com",
                "NoticeRules": [
                    {
                        "Rule": "{\"Value\":\"AND\",\"Type\":\"Operation\",\"Children\":[{\"Type\":\"Condition\",\"Value\":\"NotifyType\",\"Children\":[{\"Value\":\"In\",\"Type\":\"Compare\"},{\"Value\":\"[1,2]\",\"Type\":\"Value\"}]}]}",
                        "NoticeReceivers": [],
                        "WebCallbacks": [
                            {
                                "Url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                "CallbackType": "WeCom",
                                "Method": "",
                                "Headers": [],
                                "Body": "",
                                "Index": 1,
                                "NoticeContentId": "Default-zh",
                                "WebCallbackId": "",
                                "RemindType": 0,
                                "Mobiles": [],
                                "UserIds": []
                            }
                        ],
                        "Escalate": false,
                        "Interval": 10,
                        "Type": 1
                    }
                ],
                "DeliverStatus": 1,
                "DeliverFlag": 1,
                "AlarmNoticeDeliverConfig": null,
                "AlarmShieldStatus": 2,
                "AlarmShieldCount": {
                    "TotalCount": 0,
                    "InvalidCount": 0,
                    "ValidCount": 0,
                    "ExpireCount": 0
                },
                "CallbackPrioritize": true
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

