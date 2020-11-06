**Example 1: 词法分析示例**



Input: 

```
tccli nlp LexicalAnalysis --cli-unfold-argument  \
    --Text "欢迎使用腾讯知文自然语言处理" \
    --Flag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "8dd99adb-5144-43ca-8213-f6a929ce5075",
        "PosTokens": [
            {
                "BeginOffset": 0,
                "Word": "欢迎",
                "Length": 2,
                "Pos": "v"
            },
            {
                "BeginOffset": 2,
                "Word": "使用",
                "Length": 2,
                "Pos": "v"
            },
            {
                "BeginOffset": 4,
                "Word": "腾讯",
                "Length": 2,
                "Pos": "ntc"
            },
            {
                "BeginOffset": 6,
                "Word": "知文",
                "Length": 2,
                "Pos": "n"
            },
            {
                "BeginOffset": 8,
                "Word": "自然语言处理",
                "Length": 6,
                "Pos": "nz"
            }
        ],
        "NerTokens": [
            {
                "BeginOffset": 4,
                "Type": "ORG",
                "Word": "腾讯",
                "Length": 2
            }
        ]
    }
}
```

