**Example 1: 图像识别批改-识别**

ServerType = 0，使用识别功能，只返回识别文本（内容仅为参考，非实际返回结果）

Input: 

```
tccli ecc EHOCR --cli-unfold-argument  \
    --InputType 1 \
    --Image ccc \
    --ServerType 0
```

Output: 
```
{
    "Response": {
        "ResultData": {
            "Content": "this is compostion content",
            "CorrectData": null,
            "TaskId": null
        },
        "RequestId": "ae5d82c1-47a1-43c0-b8a2-4d3c35a21488"
    }
}
```

**Example 2: 图像识别批改-批改**

ServerType = 1，使用批改功能，返回识别文本与批改结果（内容仅为参考，非实际批改结果）

Input: 

```
tccli ecc EHOCR --cli-unfold-argument  \
    --InputType 1 \
    --Image ccc \
    --ServerType 1
```

Output: 
```
{
    "Response": {
        "ResultData": {
            "Content": "this is compostion content",
            "CorrectData": {
                "Score": 72.39,
                "ScoreCat": {
                    "Words": {
                        "Name": "词汇",
                        "Score": 76.08,
                        "Percentage": 42
                    },
                    "Sentences": {
                        "Name": "句子",
                        "Score": 61.16,
                        "Percentage": 28
                    },
                    "Structure": {
                        "Name": "篇章结构",
                        "Score": 80.37,
                        "Percentage": 23
                    },
                    "Content": {
                        "Name": "内容",
                        "Score": 69,
                        "Percentage": 7
                    },
                    "Score": 0,
                    "Percentage": 0
                },
                "Comment": "作者词汇基础扎实；可适当增加复合句和从句的使用；文中衔接词丰富。请多加练习，更上一层楼。",
                "SentenceComments": [
                    {
                        "Sentence": {
                            "Sentence": "Teenagers likeating fast 1888861 food.",
                            "ParaID": 1,
                            "SentenceID": 7
                        },
                        "Suggestions": [
                            {
                                "Type": "Error",
                                "ErrorType": "拼写错误",
                                "Origin": "likeating",
                                "Replace": "elevating",
                                "Message": "likeating 可能是拼写错误，请注意拼写检查，这里应将 likeating 替换为 elevating",
                                "ErrorPosition": [
                                    8,
                                    8
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            424,
                                            360,
                                            459,
                                            359,
                                            459,
                                            386,
                                            424,
                                            387
                                        ]
                                    }
                                ]
                            },
                            {
                                "Type": "Error",
                                "ErrorType": "易混淆词汇建议",
                                "Origin": "1888861",
                                "Replace": "1886861",
                                "Message": "注意1888861 与 1886861 的区别，推荐将 1888861 替换为 1886861",
                                "ErrorPosition": [
                                    8,
                                    8
                                ],
                                "ErrorCoordinates": [
                                    {
                                        "Coordinate": [
                                            424,
                                            360,
                                            459,
                                            359,
                                            459,
                                            386,
                                            424,
                                            387
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "TaskId": null
        },
        "RequestId": "ae5d82c1-47a1-43c0-b8a2-4d3c35a21488"
    }
}
```

**Example 3: 图像识别批改-异步**

IsAsync= 1，使用异步处理（内容仅为参考，非实际返回结果）

Input: 

```
tccli ecc EHOCR --cli-unfold-argument  \
    --InputType 1 \
    --Image ccc \
    --IsAsync 1
```

Output: 
```
{
    "Response": {
        "ResultData": {
            "Content": "",
            "CorrectData": null,
            "TaskId": "10000010"
        },
        "RequestId": "ae5d82c1-47a1-43c0-b8a2-4d3c35a21488"
    }
}
```

