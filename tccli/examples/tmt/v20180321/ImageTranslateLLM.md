**Example 1: 端到端图片翻译调用示例**

端到端图片翻译base64输入

Input: 

```
tccli tmt ImageTranslateLLM --cli-unfold-argument  \
    --Data /9j/4AAQ...FFFFABRRRQB//9k= \
    --Target zh \
    --Url None
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "Data": "iVBORw...ABJRU5ErkJggg==",
        "RequestId": "368a3dd3-e5f9-40a0-a96c-bf7db373f1de",
        "Source": "zh",
        "SourceText": "你好",
        "Target": "en",
        "TargetText": "hello",
        "TransDetails": [
            {
                "BoundingBox": {
                    "Height": 28,
                    "Width": 236,
                    "X": 118,
                    "Y": 153
                },
                "LineHeight": 28,
                "LinesCount": 1,
                "RotateParagraphRect": {
                    "Coord": [
                        {
                            "X": 118,
                            "Y": 153
                        },
                        {
                            "X": 354,
                            "Y": 153
                        },
                        {
                            "X": 354,
                            "Y": 182
                        },
                        {
                            "X": 118,
                            "Y": 182
                        }
                    ],
                    "TiltAngle": 0,
                    "Valid": false
                },
                "SourceLineText": "你好",
                "SpamCode": 0,
                "TargetLineText": "hello"
            }
        ]
    }
}
```

