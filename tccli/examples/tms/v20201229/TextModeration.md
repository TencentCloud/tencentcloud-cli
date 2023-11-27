**Example 1: 文本内容安全**



Input: 

```
tccli tms TextModeration --cli-unfold-argument  \
    --Content 5Yqg5oiR5aW95Y+LIOe7meS9oOS8mOaDoOWIuA== \
    --BizType test
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "BizType": "test",
        "Label": "Ad",
        "SubLabel": "",
        "Suggestion": "Block",
        "Keywords": [
            "优惠券"
        ],
        "Score": 100,
        "DataId": "CSFb_MJRV5piaczW",
        "DetailResults": [
            {
                "Label": "Polity",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": [],
                "Score": 0,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null,
                "HitInfos": []
            },
            {
                "Label": "Ad",
                "SubLabel": "",
                "Suggestion": "Block",
                "Keywords": [
                    "优惠券"
                ],
                "Score": 100,
                "LibType": 2,
                "LibId": "",
                "LibName": "",
                "Tags": null,
                "HitInfos": [
                    {
                        "Type": "Keyword",
                        "Keyword": "优惠券",
                        "LibName": "default_1_0_1256309736_100004528167",
                        "Positions": [
                            {
                                "Start": 7,
                                "End": 10
                            }
                        ]
                    }
                ]
            },
            {
                "Label": "Abuse",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": [],
                "Score": 0,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null,
                "HitInfos": []
            },
            {
                "Label": "Illegal",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": [],
                "Score": 0,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null,
                "HitInfos": []
            },
            {
                "Label": "Terror",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": [],
                "Score": 0,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null,
                "HitInfos": []
            },
            {
                "Label": "Porn",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": [],
                "Score": 2,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null,
                "HitInfos": []
            }
        ],
        "RiskDetails": null,
        "Extra": "",
        "ContextText": "",
        "SentimentAnalysis": {}
    }
}
```

