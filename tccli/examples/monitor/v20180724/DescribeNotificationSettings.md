**Example 1: 测试环境真实示例**



Input: 

```
tccli monitor DescribeNotificationSettings --cli-unfold-argument  \
    --MonitorType MT_CLS \
    --PageParams.PerPage 10 \
    --PageParams.PageNo 1
```

Output: 
```
{
    "Response": {
        "PageResult": {
            "CurrentPageNo": 1,
            "IsEnd": true,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "91e283df-c1c2-435d-a766-62a0455b57bf",
        "Settings": [
            {
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
                "SettingId": "ntfs-3c5yw37f4oopcb9n"
            }
        ]
    }
}
```

