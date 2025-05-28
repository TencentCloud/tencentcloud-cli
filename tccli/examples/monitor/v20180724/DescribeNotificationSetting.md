**Example 1: 测试环境真实示例**



Input: 

```
tccli monitor DescribeNotificationSetting --cli-unfold-argument  \
    --MonitorType MT_CLS \
    --SettingId ntfs-naqf3gjd6k5nzaj4
```

Output: 
```
{
    "Response": {
        "RequestId": "3ece1619-b169-4ecc-b5a5-a731778d1876",
        "Setting": {
            "EscalationRules": [
                {
                    "AfterLastPartSeconds": 3000,
                    "CheckPoints": [],
                    "Notices": [
                        {
                            "ContentTmplId": "tmpl-erictest11",
                            "Levels": [
                                "None"
                            ],
                            "NoticeId": "notice-erictest11"
                        },
                        {
                            "ContentTmplId": "tmpl-erictest12",
                            "Levels": [
                                "None"
                            ],
                            "NoticeId": "notice-erictest12"
                        }
                    ],
                    "PartSeqNum": 1
                },
                {
                    "AfterLastPartSeconds": 5000,
                    "CheckPoints": [],
                    "Notices": [
                        {
                            "ContentTmplId": "tmpl-erictest21",
                            "Levels": [
                                "None"
                            ],
                            "NoticeId": "notice-erictest21"
                        }
                    ],
                    "PartSeqNum": 2
                }
            ],
            "Frequency": 0,
            "HasEscalation": true,
            "MatchById": "policy-erictest2",
            "MatchParams": "",
            "MatchType": "PolicyOneOnOne",
            "MonitorType": "",
            "Notices": [],
            "SettingId": "ntfs-naqf3gjd6k5nzaj4"
        }
    }
}
```

