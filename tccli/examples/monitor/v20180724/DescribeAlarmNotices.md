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
                "Id": "notice-id",
                "Name": "notice-name",
                "UpdatedAt": "2020-10-10 10:10:10",
                "UpdatedBy": "2020-10-10 10:10:10",
                "NoticeType": "normal",
                "UserNotices": [
                    {
                        "ReceiverType": "webhook",
                        "UserIds": [
                            0
                        ],
                        "GroupIds": [
                            0
                        ],
                        "StartTime": 0,
                        "EndTime": 0,
                        "NoticeWay": [
                            ""
                        ],
                        "PhoneOrder": [
                            0
                        ],
                        "PhoneCircleTimes": 0,
                        "PhoneInnerInterval": 0,
                        "PhoneCircleInterval": 0,
                        "NeedPhoneArriveNotice": 0,
                        "PhoneCallType": "",
                        "Weekday": [
                            0
                        ],
                        "OnCallFormIDs": [
                            ""
                        ]
                    }
                ],
                "URLNotices": [
                    {
                        "URL": "",
                        "IsValid": 0,
                        "ValidationCode": "",
                        "StartTime": 0,
                        "EndTime": 0,
                        "Weekday": [
                            0
                        ]
                    }
                ],
                "IsPreset": 0,
                "NoticeLanguage": "",
                "PolicyIds": [
                    ""
                ],
                "AMPConsumerId": "",
                "CLSNotices": [
                    {
                        "Enable": 0,
                        "Region": "",
                        "LogSetId": "",
                        "TopicId": ""
                    }
                ],
                "Tags": [
                    {
                        "Key": "",
                        "Value": ""
                    }
                ]
            }
        ],
        "RequestId": "xyz"
    }
}
```

