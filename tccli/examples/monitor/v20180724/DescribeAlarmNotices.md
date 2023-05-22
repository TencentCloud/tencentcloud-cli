**Example 1: 查询通知模板列表**

查询通知模板列表

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
        "TotalCount": 0,
        "Notices": [
            {
                "Id": "abc",
                "Name": "abc",
                "UpdatedAt": "abc",
                "UpdatedBy": "abc",
                "NoticeType": "abc",
                "UserNotices": [
                    {
                        "ReceiverType": "abc",
                        "UserIds": [
                            0
                        ],
                        "GroupIds": [
                            0
                        ],
                        "StartTime": 0,
                        "EndTime": 0,
                        "NoticeWay": [
                            "abc"
                        ],
                        "PhoneOrder": [
                            0
                        ],
                        "PhoneCircleTimes": 0,
                        "PhoneInnerInterval": 0,
                        "PhoneCircleInterval": 0,
                        "NeedPhoneArriveNotice": 0,
                        "PhoneCallType": "abc",
                        "Weekday": [
                            0
                        ],
                        "OnCallFormIDs": [
                            "abc"
                        ]
                    }
                ],
                "URLNotices": [
                    {
                        "URL": "abc",
                        "IsValid": 0,
                        "ValidationCode": "abc",
                        "StartTime": 0,
                        "EndTime": 0,
                        "Weekday": [
                            0
                        ]
                    }
                ],
                "IsPreset": 0,
                "NoticeLanguage": "abc",
                "PolicyIds": [
                    "abc"
                ],
                "AMPConsumerId": "abc",
                "CLSNotices": [
                    {
                        "Enable": 0,
                        "Region": "abc",
                        "LogSetId": "abc",
                        "TopicId": "abc"
                    }
                ],
                "Tags": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

