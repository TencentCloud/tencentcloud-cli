**Example 1: 通用文本图像告警示例代码**

通用文本图像告警示例

Input: 

```
tccli ocr RecognizeGeneralTextImageWarn --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Blur": {
            "IsWarn": false,
            "Polygon": [],
            "SpecificMatter": ""
        },
        "BorderIncomplete": {
            "IsWarn": false,
            "Polygon": [],
            "SpecificMatter": ""
        },
        "Copy": {
            "IsWarn": true,
            "Polygon": [
                {
                    "LeftBottom": {
                        "X": 0,
                        "Y": 0
                    },
                    "LeftTop": {
                        "X": 0,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": 0,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": 0,
                        "Y": 0
                    }
                }
            ],
            "SpecificMatter": ""
        },
        "Reflection": {
            "IsWarn": false,
            "Polygon": [],
            "SpecificMatter": ""
        },
        "Reprint": {
            "IsWarn": true,
            "Polygon": [
                {
                    "LeftBottom": {
                        "X": 0,
                        "Y": 0
                    },
                    "LeftTop": {
                        "X": 0,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": 0,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": 0,
                        "Y": 0
                    }
                }
            ],
            "SpecificMatter": ""
        },
        "RequestId": "d8b2bf40-091e-43f1-a075-d98a5c9b2e1e"
    }
}
```

