**Example 1: 速算题目批改-同步模式**

同步模式，直接返回结果，TaskId 为空

Input: 

```
tccli hcm Evaluation --cli-unfold-argument  \
    --SessionId s_1596611058609_2868392 \
    --Url xxx
```

Output: 
```
{
    "Response": {
        "SessionId": "s_1596611058609_2868392",
        "Items": [
            {
                "Item": "YES",
                "ItemString": "600*5=6*500",
                "ItemConf": 0,
                "ItemCoord": {
                    "Height": 130,
                    "Width": 531,
                    "X": 1135,
                    "Y": 953
                },
                "Answer": "",
                "ExpressionType": "1",
                "QuestionId": ""
            },
            {
                "Item": "YES",
                "ItemString": "4厘米=(40)毫米",
                "ItemConf": 0,
                "ItemCoord": {
                    "Height": 125,
                    "Width": 579,
                    "X": 1489,
                    "Y": 800
                },
                "Answer": "",
                "ExpressionType": "7",
                "QuestionId": ""
            }
        ],
        "RequestId": "17c1a0ba-0b66-4b28-892f-f248dcc5f548",
        "TaskId": ""
    }
}
```

**Example 2: 速算题目批改-异步模式**

异步模式，只返回 TaskId

Input: 

```
tccli hcm Evaluation --cli-unfold-argument  \
    --SessionId stress_test_956938 \
    --Url xxx \
    --IsAsync 1
```

Output: 
```
{
    "Response": {
        "SessionId": "1112asdfasdf1",
        "Items": null,
        "TaskId": "1000010",
        "RequestId": "55ad4928-fa5-415c-2cb-868d5e3171431"
    }
}
```

