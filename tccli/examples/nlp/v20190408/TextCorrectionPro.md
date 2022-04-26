**Example 1: 文本纠错示例**



Input: 

```
tccli nlp TextCorrectionPro --cli-unfold-argument  \
    --Text "令天天气很好，我们很早起床，去学小读书。"
```

Output: 
```
{
    "Response": {
        "RequestId": "8dd99adb-5144-43ca-8213-f6a929ce5075",
        "CCITokens": [
            {
                "BeginOffset": 0,
                "Word": "令",
                "CorrectWord": "今"
            },
            {
                "BeginOffset": 16,
                "Word": "小",
                "CorrectWord": "校"
            }
        ],
        "ResultText": "今天天气很好，我们很早起床，去学校读书。"
    }
}
```

