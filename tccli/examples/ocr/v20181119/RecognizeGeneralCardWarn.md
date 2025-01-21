**Example 1: 通用卡证ps检测告警**

身份证

Input: 

```
tccli ocr RecognizeGeneralCardWarn --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardOCR/IDCardOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Blur": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "BorderIncomplete": {
            "IsWarn": true,
            "Polygon": [],
            "RiskConfidence": 0.99
        },
        "CardType": "idcard",
        "Copy": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Ps": {
            "IsWarn": true,
            "Polygon": [
                {
                    "LeftBottom": {
                        "X": 679,
                        "Y": 524
                    },
                    "LeftTop": {
                        "X": 679,
                        "Y": 86
                    },
                    "RightBottom": {
                        "X": 985,
                        "Y": 524
                    },
                    "RightTop": {
                        "X": 985,
                        "Y": 86
                    }
                },
                {
                    "LeftBottom": {
                        "X": 377,
                        "Y": 627
                    },
                    "LeftTop": {
                        "X": 377,
                        "Y": 582
                    },
                    "RightBottom": {
                        "X": 947,
                        "Y": 627
                    },
                    "RightTop": {
                        "X": 947,
                        "Y": 582
                    }
                },
                {
                    "LeftBottom": {
                        "X": 205,
                        "Y": 135
                    },
                    "LeftTop": {
                        "X": 205,
                        "Y": 93
                    },
                    "RightBottom": {
                        "X": 288,
                        "Y": 135
                    },
                    "RightTop": {
                        "X": 288,
                        "Y": 93
                    }
                },
                {
                    "LeftBottom": {
                        "X": 206,
                        "Y": 307
                    },
                    "LeftTop": {
                        "X": 206,
                        "Y": 269
                    },
                    "RightBottom": {
                        "X": 297,
                        "Y": 307
                    },
                    "RightTop": {
                        "X": 297,
                        "Y": 269
                    }
                },
                {
                    "LeftBottom": {
                        "X": 206,
                        "Y": 221
                    },
                    "LeftTop": {
                        "X": 206,
                        "Y": 183
                    },
                    "RightBottom": {
                        "X": 244,
                        "Y": 221
                    },
                    "RightTop": {
                        "X": 244,
                        "Y": 183
                    }
                },
                {
                    "LeftBottom": {
                        "X": 198,
                        "Y": 402
                    },
                    "LeftTop": {
                        "X": 198,
                        "Y": 359
                    },
                    "RightBottom": {
                        "X": 649,
                        "Y": 402
                    },
                    "RightTop": {
                        "X": 649,
                        "Y": 359
                    }
                },
                {
                    "LeftBottom": {
                        "X": 630,
                        "Y": 623
                    },
                    "LeftTop": {
                        "X": 630,
                        "Y": 582
                    },
                    "RightBottom": {
                        "X": 661,
                        "Y": 623
                    },
                    "RightTop": {
                        "X": 661,
                        "Y": 582
                    }
                }
            ],
            "RiskConfidence": 0.7648103
        },
        "Reflection": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.04
        },
        "Reprint": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "RequestId": "b4bdbf23-9788-413f-90b4-ffe2cedf773b"
    }
}
```

