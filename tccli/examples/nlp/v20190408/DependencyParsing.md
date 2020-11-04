**Example 1: 句法依存分析示例**



Input: 

```
tccli nlp DependencyParsing --cli-unfold-argument  \
    --Text "飞蛾扑火似地牺牲演出"
```

Output: 
```
{
    "Response": {
        "RequestId": "8dd99adb-5144-43ca-7113-f6a929ce5076",
        "DpTokens": [
            {
                "Word": "演出",
                "Id": 4,
                "HeadId": 3,
                "Relation": "并列关系"
            },
            {
                "Word": "牺牲",
                "Id": 3,
                "HeadId": 1,
                "Relation": "并列关系"
            },
            {
                "Word": "似地",
                "Id": 2,
                "HeadId": 1,
                "Relation": "右附加关系"
            },
            {
                "Word": "飞蛾扑火",
                "Id": 1,
                "HeadId": 0,
                "Relation": "核心关系"
            }
        ]
    }
}
```

