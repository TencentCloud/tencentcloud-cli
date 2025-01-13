**Example 1: 通用文本图像告警示例代码**

通用文本图像告警示例

Input: 

```
tccli ocr RecognizeGeneralTextImageWarn --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/RecognizeGeneralTextImageWarn/RecognizeGeneralTextImageWarn1.png \
    --Type General
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
            "IsWarn": false,
            "Polygon": [],
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
        "RequestId": "20bbcd54-6e63-4140-b777-2dea85a8ef66"
    }
}
```

