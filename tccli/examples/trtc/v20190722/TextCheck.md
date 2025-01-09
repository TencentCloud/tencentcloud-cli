**Example 1: 文本审核1**

文本审核1

Input: 

```
tccli trtc TextCheck --cli-unfold-argument  \
    --Content 违法词 \
    --SdkAppId 140018366 \
    --Source 0
```

Output: 
```
{
    "Response": {
        "CheckDetails": [
            {
                "Label": "polity",
                "Label2": 1
            }
        ],
        "Label": "polity",
        "RequestId": "8022ae26-4a64-4112-bd89-675630be2184",
        "Score": 91,
        "Suggestion": 2
    }
}
```

