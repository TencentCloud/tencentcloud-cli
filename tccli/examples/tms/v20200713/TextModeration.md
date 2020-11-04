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
        "RequestId": "46f504df-d9ac-4fc0-899f-58020d8abd19",
        "BizType": "11",
        "EvilFlag": 1,
        "Label": "Custom",
        "Suggestion": "Block",
        "Keywords": [
            "加我微信"
        ],
        "Score": 87,
        "DetailResults": [
            {
                "Label": "Ads",
                "Suggestion": "Block",
                "Keywords": [
                    "加我微信",
                    "扫码分享领红包",
                    "购买链接：xxxxxxx"
                ],
                "Score": 72
            },
            {
                "Label": "Custom",
                "Suggestion": "Block",
                "Keywords": [
                    "手机号码xxxxxxxxxxx"
                ],
                "Score": 0,
                "LibType": 2,
                "LibId": "20548499",
                "LibName": "priavte"
            }
        ],
        "RiskDetails": [
            {
                "Lable": "RiskAccount",
                "Level": 2
            }
        ],
        "Extra": "{\"KeywordsInfo\":[{\"HitInfo\":\"加微信\",\"Label\":\"Ad\",\"LabelCode\":\"20105\",\"SubLabelCode\":\"20105201\"}]}"
    },
    "retcode": 0,
    "retmsg": ""
}
```

