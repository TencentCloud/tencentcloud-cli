**Example 1: 文本内容安全**



Input: 

```
tccli tms TextModeration --cli-unfold-argument  \
    --Content 5L2g55qE5Lil6LCo6K6p5L2g5Y+R546w77yM5Lqn5ZOB57uP55CG5Y+r5YmR6Z2S
```

Output: 
```
{
    "Response": {
        "RequestId": "be7474bf-bcc6-4f4b-a081-80ac687c040e",
        "BizType": "content_input",
        "Label": "Illegal",
        "SubLabel": "Drug",
        "Suggestion": "Block",
        "Keywords": [],
        "Score": 87,
        "DataId": "YIumnjV2MZibqk6G",
        "DetailResults": [
            {
                "Label": "Illegal",
                "SubLabel": "Drug",
                "Suggestion": "Block",
                "Keywords": [],
                "Score": 87,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null,
                "HitInfos": [
                    {
                        "Type": "Keyword",
                        "Keyword": "你好呀",
                        "LibName": "",
                        "Positions": [
                            {
                                "Start": 0,
                                "End": 3
                            }
                        ]
                    },
                    {
                        "Type": "Model",
                        "Keyword": "",
                        "LibName": "",
                        "Positions": [
                            {
                                "Start": 0,
                                "End": 3
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
                "Label": "Ad",
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
                "Label": "Teenager",
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
                "Label": "Value",
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
            }
        ],
        "RiskDetails": null,
        "Extra": "",
        "ContextText": "",
        "SentimentAnalysis": {},
        "HitType": "text_nlp_tianji",
        "HitSnippetInfos": [
            {
                "Snippet": "你好呀",
                "AtomicName": "",
                "AtomicId": "",
                "Positions": [
                    {
                        "Start": 0,
                        "End": 3
                    }
                ]
            }
        ]
    }
}
```

