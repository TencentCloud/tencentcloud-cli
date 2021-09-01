**Example 1: 文本内容安全**



Input: 

```
tccli tms TextModeration --cli-unfold-argument  \
    --Content 57uY5aOw57uY6Imy
```

Output: 
```
{
    "Response": {
        "DataId": "123",
        "Extra": "xx",
        "BizType": "0",
        "RiskDetails": [
            {
                "Level": 2,
                "Label": "RiskAccount"
            }
        ],
        "DetailResults": [
            {
                "LibName": "Porn",
                "Score": 72,
                "Label": "Porn",
                "LibId": "12",
                "Suggestion": "Review",
                "Keywords": [
                    "色情"
                ],
                "LibType": 0
            },
            {
                "LibName": "Porn",
                "Score": 0,
                "Label": "",
                "LibId": "1",
                "Suggestion": "Block",
                "Keywords": [
                    "色情"
                ],
                "LibType": 2
            }
        ],
        "Label": "Ad",
        "EvilFlag": 1,
        "Score": 87,
        "RequestId": "x2123-123123-123",
        "Suggestion": "Block",
        "Keywords": [
            "加我好友，给你发优惠券"
        ]
    }
}
```

