**Example 1: 查询通知模板列表**



Input: 

```
tccli monitor DescribeAlarmNotices --cli-unfold-argument  \
    --OwnerUid 1234567 \
    --Module monitor \
    --Name  \
    --ReceiverType  \
    --PageNumber 1 \
    --PageSize 20 \
    --Order DESC \
    --NoticeIds notice-ah28cv9d
```

Output: 
```
{
    "Response": {
        "Notices": [
            {
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
                    }
                ],
                "Name": "xx",
                "NoticeType": "xx",
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "CLSNotices": [
                    {
                        "TopicId": "xx",
                        "Region": "xx",
                        "Enable": 0,
                        "LogSetId": "xx"
                    }
                ],
                "PolicyIds": [
                    "xx"
                ],
                "UserNotices": [
                    {
                        "NoticeWay": [
                            "SMS",
                            "EMAIL"
                        ],
                        "NeedPhoneArriveNotice": 0,
                        "PhoneOrder": [
                            0
                        ],
                        "PhoneCallType": "xx",
                        "UserIds": [
                            1234567
                        ],
                        "ReceiverType": "xx",
                        "PhoneCircleInterval": 0,
                        "GroupIds": [
                            0
                        ],
                        "StartTime": 0,
                        "PhoneCircleTimes": 0,
                        "EndTime": 86399,
                        "PhoneInnerInterval": 0,
                        "Weekday": [
                            0
                        ]
                    }
                ],
                "IsPreset": 1,
                "UpdatedBy": "xx",
                "UpdatedAt": "xx",
                "NoticeLanguage": "xx",
                "Id": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

