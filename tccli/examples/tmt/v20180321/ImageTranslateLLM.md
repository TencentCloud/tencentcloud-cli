**Example 1: 图片翻译调用示例**



Input: 

```
tccli tmt ImageTranslateLLM --cli-unfold-argument  \
    --Data iVBORw0KGgoAAAAN......Ws0ewAAAABJRU5ErkJggg== \
    --Target en
```

Output: 
```
{
    "Response": {
        "Data": "iVBORw0KGgoAAAANSUh......4AAAAASUVORK5CYII=",
        "RequestId": "962cc025-f31c-466a-9a2d-c7947bd866c2",
        "Source": "zh_CN",
        "SourceText": "你好",
        "Target": "en",
        "TargetText": "Hello"
    }
}
```

**Example 2: 成功示例2**

成功示例2

Input: 

```
tccli tmt ImageTranslateLLM --cli-unfold-argument  \
    --Data "" \
    --Target en \
    --Url https://xxx.com/image.jpg
```

Output: 
```
{
    "Response": {
        "Angle": 90,
        "Data": "iVBORw0KGgoAAAANSUh......4AAAAASUVORK5CYII=",
        "RequestId": "d434a671-2835-4bed-a3c3-66becaf6a50c",
        "Source": "zh_CN",
        "SourceText": "你好",
        "Target": "en",
        "TargetText": "hello",
        "TransDetails": [
            {
                "BoundingBox": {
                    "Height": 34,
                    "Width": 202,
                    "X": 37,
                    "Y": 57
                },
                "LineHeight": 15,
                "LinesCount": 1,
                "SourceLineText": "你好",
                "TargetLineText": "hello"
            }
        ]
    }
}
```

