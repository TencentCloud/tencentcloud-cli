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
                "SubLabel": "SexualBehavior",
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
        "SubLabel": "Contact",
        "Score": 87,
        "RequestId": "x2123-123123-123",
        "Suggestion": "Block",
        "Keywords": [
            "加我好友，给你发优惠券"
        ],
        "ContextText": "加我好友 给你优惠券"
    }
}
```

**Example 2: 文本内容安全示例**



Input: 

```
tccli tms TextModeration --cli-unfold-argument  \
    --Content 5LusCg \
    --BizType bigotest \
    --User.RoomId 字符串 \
    --User.ReceiverId 123 \
    --User.UserId user1
```

Output: 
```
{
    "Response": {
        "RequestId": "7f54771f-9b67-4b55-9ac9-77b1a0f4dc37",
        "BizType": "bigotest",
        "Label": "Normal",
        "SubLabel": "",
        "Suggestion": "Pass",
        "Keywords": [],
        "Score": 0,
        "DataId": "",
        "DetailResults": [
            {
                "Label": "Porn",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": null,
                "Score": 0,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null
            },
            {
                "Label": "Abuse",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": null,
                "Score": 0,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null
            },
            {
                "Label": "Ad",
                "SubLabel": "",
                "Suggestion": "Pass",
                "Keywords": null,
                "Score": 0,
                "LibType": 0,
                "LibId": "",
                "LibName": "",
                "Tags": null
            }
        ],
        "RiskDetails": null,
        "Extra": "",
        "ContextText": ""
    },
    "retcode": 0,
    "retmsg": ""
}
```

