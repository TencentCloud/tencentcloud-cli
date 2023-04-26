**Example 1: 词法分析调用示例**

词法分析

Input: 

```
tccli nlp ParseWords --cli-unfold-argument  \
    --Text 我很喜欢看流浪地球这个电影
```

Output: 
```
{
    "Response": {
        "BasicParticiples": [
            {
                "BeginOffset": 0,
                "Length": 1,
                "Pos": "PN",
                "Word": "我"
            },
            {
                "BeginOffset": 1,
                "Length": 1,
                "Pos": "AD",
                "Word": "很"
            },
            {
                "BeginOffset": 2,
                "Length": 2,
                "Pos": "VV",
                "Word": "喜欢"
            },
            {
                "BeginOffset": 4,
                "Length": 1,
                "Pos": "VV",
                "Word": "看"
            },
            {
                "BeginOffset": 5,
                "Length": 2,
                "Pos": "VV",
                "Word": "流浪"
            },
            {
                "BeginOffset": 7,
                "Length": 2,
                "Pos": "NN",
                "Word": "地球"
            },
            {
                "BeginOffset": 9,
                "Length": 2,
                "Pos": "DT",
                "Word": "这个"
            },
            {
                "BeginOffset": 11,
                "Length": 2,
                "Pos": "NN",
                "Word": "电影"
            }
        ],
        "CompoundParticiples": [
            {
                "BeginOffset": 0,
                "Length": 1,
                "Pos": "PN",
                "Word": "我"
            },
            {
                "BeginOffset": 1,
                "Length": 1,
                "Pos": "AD",
                "Word": "很"
            },
            {
                "BeginOffset": 2,
                "Length": 2,
                "Pos": "VV",
                "Word": "喜欢"
            },
            {
                "BeginOffset": 4,
                "Length": 1,
                "Pos": "VV",
                "Word": "看"
            },
            {
                "BeginOffset": 5,
                "Length": 4,
                "Pos": "NN",
                "Word": "流浪地球"
            },
            {
                "BeginOffset": 9,
                "Length": 2,
                "Pos": "DT",
                "Word": "这个"
            },
            {
                "BeginOffset": 11,
                "Length": 2,
                "Pos": "NN",
                "Word": "电影"
            }
        ],
        "Entities": [
            {
                "BeginOffset": 5,
                "Length": 4,
                "Name": "电影",
                "Type": "work.movie",
                "Word": "流浪地球"
            }
        ],
        "NormalText": "我很喜欢看流浪地球这个电影",
        "RequestId": "6cd06531-5b5e-46ee-8ec2-ab66a9730e74"
    }
}
```

