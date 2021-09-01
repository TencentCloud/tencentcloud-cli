**Example 1: 文本分类示例**



Input: 

```
tccli nlp TextClassification --cli-unfold-argument  \
    --Text "为迎接下周的比赛，今日巴萨队又开始了集训。" \
    --Flag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "8dd99adb-5144-43ca-8213-f6a929ce5075",
        "Classes": [
            {
                "FirstClassName": "体育",
                "FirstClassProbability": 1,
                "SecondClassName": "西甲",
                "SecondClassProbability": 1
            }
        ]
    }
}
```

