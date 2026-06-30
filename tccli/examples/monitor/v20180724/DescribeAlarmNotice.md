**Example 1: 查询单个通知模板的详情**

查询告警通知模板ID为"notice-2g892hg8"的告警通知模板详情

Input: 

```
tccli monitor DescribeAlarmNotice --cli-unfold-argument  \
    --Module monitor \
    --NoticeId notice-2g892hg8
```

Output: 
```
{
    "Response": {
        "Notice": {
            "AMPConsumerId": "Consumer-*x****f***",
            "CLSNotices": [],
            "Id": "notice-60vrut83",
            "IsLoginFree": 0,
            "IsPreset": 0,
            "Name": "auto-dy5r8i",
            "NoticeLanguage": "zh-CN",
            "NoticeType": "ALL",
            "PolicyIds": [
                "policy-********"
            ],
            "Tags": null,
            "TimeZoneName": "",
            "URLNotices": [],
            "UpdatedAt": "2026-06-29 14:02:49",
            "UpdatedBy": "10002*******",
            "UserNotices": [
                {
                    "EndTime": 86399,
                    "GroupIds": [
                        309306
                    ],
                    "NeedPhoneArriveNotice": 1,
                    "NoticeWay": [
                        "SMS",
                        "EMAIL"
                    ],
                    "OnCallFormIDs": [
                        ""
                    ],
                    "PhoneCallType": "CIRCLE",
                    "PhoneCircleInterval": 180,
                    "PhoneCircleTimes": 1,
                    "PhoneInnerInterval": 180,
                    "PhoneOrder": null,
                    "ReceiverType": "GROUP",
                    "StartTime": 0,
                    "UserIds": null,
                    "VoiceConfirmKey": "",
                    "Weekday": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7
                    ]
                }
            ]
        },
        "RequestId": "4aa5868c-35a1-49f0-b639-f9c85cbc904c"
    }
}
```

