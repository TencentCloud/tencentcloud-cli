**Example 1: 查询通知模板列表**



Input: 

```
tccli monitor DescribeAlarmNotices --cli-unfold-argument  \
    --OwnerUid 1234567 \
    --Name  \
    --ReceiverType  \
    --PageNumber 1 \
    --PageSize 20 \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "Notices": [
            {
                "Id": "notice-lc0bjcrq",
                "Name": "系统预设通知模板",
                "UpdatedAt": "2020-10-15 22:42:32",
                "UpdatedBy": "789789789",
                "NoticeType": "ALL",
                "UserNotices": [
                    {
                        "ReceiverType": "USER",
                        "UserIds": [
                            1234567
                        ],
                        "GroupIds": null,
                        "StartTime": 0,
                        "EndTime": 86399,
                        "NoticeWay": [
                            "SMS",
                            "EMAIL"
                        ],
                        "PhoneOrder": null,
                        "PhoneCircleTimes": 0,
                        "PhoneInnerInterval": 0,
                        "PhoneCircleInterval": 0,
                        "NeedPhoneArriveNotice": 0
                    }
                ],
                "URLNotices": [],
                "IsPreset": 1,
                "NoticeLanguage": "zh-CN",
                "PolicyIds": []
            }
        ],
        "RequestId": "mcy414ov4yom5l9lcam6phul347qqv41",
        "TotalCount": 1
    }
}
```

