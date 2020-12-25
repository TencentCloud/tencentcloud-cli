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
        "RequestId": "fasdfaghash434stsi579ah",
        "Notice": {
            "Id": "notice-2g892hg8",
            "Name": "测试-告警通知规则1",
            "UpdatedAt": "2020-05-01 12:00:00",
            "UpdatedBy": "112051051047",
            "NoticeType": "ALL",
            "NoticeLanguage": "zh-CN",
            "UserNotices": [
                {
                    "ReceiverType": "USER",
                    "UserIds": [
                        168105,
                        162208
                    ],
                    "GroupIds": [],
                    "StartTime": 0,
                    "EndTime": 3600,
                    "NoticeWay": [
                        "EMAIL",
                        "CALL"
                    ],
                    "PhoneOrder": [
                        162208,
                        168105
                    ],
                    "PhoneCircleTimes": 2,
                    "PhoneInnerInterval": 60,
                    "PhoneCircleInterval": 60,
                    "NeedPhoneArriveNotice": 1
                }
            ],
            "URLNotices": [
                {
                    "URL": "http://www.baidu.com/validate",
                    "IsValid": 0,
                    "ValidationCode": "1r51tg3"
                },
                {
                    "URL": "https://www.googe.com/validate",
                    "IsValid": 0,
                    "ValidationCode": "h4224"
                }
            ],
            "IsPreset": 0,
            "PolicyIds": [
                "policy-58hbt18"
            ]
        }
    }
}
```

