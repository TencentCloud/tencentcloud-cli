**Example 1: 调用示例**



Input: 

```
tccli tmt ImageTranslateLLM --cli-unfold-argument  \
    --Data /9j/4AAQSkZJRg...rF530LvvALAD5Mkgv0ULqKbuJJbW5en/9k= \
    --Target en \
    --Url None
```

Output: 
```
{
    "Response": {
        "Angle": 270,
        "Data": "/9j/4AAQSkZJRg...rF530LvvALAD5Mkgv0ULqKbuJJbW5en/9k=",
        "RequestId": "defb956d-xxxx-xxxx-xxxx-2595b7bc2c28",
        "Source": "en",
        "SourceText": "hello.",
        "Target": "zh",
        "TargetText": "你好。",
        "TransDetails": [
            {
                "BoundingBox": {
                    "Height": 90,
                    "Width": 518,
                    "X": 348,
                    "Y": 147
                },
                "LineHeight": 0,
                "LinesCount": 0,
                "RotateParagraphRect": {
                    "Coord": [
                        {
                            "X": 348,
                            "Y": 147
                        },
                        {
                            "X": 866,
                            "Y": 147
                        },
                        {
                            "X": 866,
                            "Y": 238
                        },
                        {
                            "X": 348,
                            "Y": 238
                        }
                    ],
                    "TiltAngle": 0,
                    "Valid": false
                },
                "SourceLineText": "hello.",
                "SpamCode": 0,
                "TargetLineText": "你好。"
            }
        ]
    }
}
```

