**Example 1: 纯文本英语作文批改-同步**

IsAsync=0 时为同步模式，返回批改结果（内容仅为参考，非实际批改结果）

Input: 

```
tccli ecc ECC --cli-unfold-argument  \
    --Content abc \
    --Title abc \
    --Grade abc \
    --Requirement abc \
    --ModelTitle abc \
    --ModelContent abc \
    --EccAppid abc \
    --IsAsync 0 \
    --SessionId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Score": 0,
            "ScoreCat": {
                "Words": {
                    "Name": "abc",
                    "Score": 0,
                    "Percentage": 0
                },
                "Sentences": {
                    "Name": "abc",
                    "Score": 0,
                    "Percentage": 0
                },
                "Structure": {
                    "Name": "abc",
                    "Score": 0,
                    "Percentage": 0
                },
                "Score": 0,
                "Percentage": 0
            },
            "Comment": "abc",
            "SentenceComments": [
                {
                    "Suggestions": [
                        {
                            "Type": "abc",
                            "ErrorType": "abc",
                            "Origin": "abc",
                            "Replace": "abc",
                            "Message": "abc",
                            "ErrorPosition": [
                                0
                            ],
                            "ErrorCoordinates": [
                                {
                                    "Coordinate": [
                                        0
                                    ]
                                }
                            ]
                        }
                    ],
                    "Sentence": {
                        "Sentence": "abc",
                        "ParaID": 0,
                        "SentenceID": 0
                    }
                }
            ]
        },
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

**Example 2: 纯文本英语作文批改-异步**

IsAsync=1 时为异步模式，返回 TaskId（内容仅为参考，非实际返回结果）

Input: 

```
tccli ecc ECC --cli-unfold-argument  \
    --Content abc \
    --Title abc \
    --Grade abc \
    --Requirement abc \
    --ModelTitle abc \
    --ModelContent abc \
    --EccAppid abc \
    --IsAsync 0 \
    --SessionId abc
```

Output: 
```
{
    "Response": {
        "Data": null,
        "TaskId": "10000004",
        "RequestId": "ae5d82c1-47a1-43c0-b8a2-4d3c35a21488"
    }
}
```

