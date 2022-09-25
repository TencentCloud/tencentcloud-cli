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
            "AMPConsumerId": "xx",
            "URLNotices": [
                {
                    "ValidationCode": "xx",
                    "URL": "xx",
                    "IsValid": 0,
                    "Weekday": [
                        0
                    ],
                    "StartTime": 0,
                    "EndTime": 0
                },
                {
                    "ValidationCode": "xx",
                    "URL": "xx",
                    "IsValid": 0,
                    "Weekday": [
                        0
                    ],
                    "StartTime": 0,
                    "EndTime": 0
                }
            ],
            "Name": "xx",
            "NoticeType": "xx",
            "CLSNotices": [
                {
                    "TopicId": "xx",
                    "Region": "xx",
                    "Enable": 0,
                    "LogSetId": "xx"
                }
            ],
            "UpdatedBy": "xx",
            "PolicyIds": [
                "policy-58hbt18"
            ],
            "UserNotices": [
                {
                    "NoticeWay": [
                        "EMAIL",
                        "CALL"
                    ],
                    "NeedPhoneArriveNotice": 1,
                    "PhoneOrder": [
                        162208,
                        168105
                    ],
                    "PhoneCallType": "xx",
                    "UserIds": [
                        168105,
                        162208
                    ],
                    "ReceiverType": "xx",
                    "PhoneCircleInterval": 60,
                    "GroupIds": [
                        0
                    ],
                    "StartTime": 0,
                    "PhoneCircleTimes": 2,
                    "EndTime": 3600,
                    "PhoneInnerInterval": 60,
                    "Weekday": [
                        0
                    ]
                }
            ],
            "IsPreset": 0,
            "UpdatedAt": "xx",
            "NoticeLanguage": "xx",
            "Id": "xx"
        },
        "RequestId": "xx"
    }
}
```

