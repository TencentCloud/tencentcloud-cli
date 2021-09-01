**Example 1: 调用失败示例**



Input: 

```
tccli bda DetectBody --cli-unfold-argument  \
    --Url IamNotUrl
```

Output: 
```
{
    "Response": {
        "RequestId": "b5f77c78-efaf-42d1-b0ac-419cc70b4994"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda DetectBody --cli-unfold-argument  \
    --Url test.jpg
```

Output: 
```
{
    "Response": {
        "BodyDetectResults": [
            {
                "BodyRect": {
                    "X": 260,
                    "Y": 1,
                    "Width": 272,
                    "Height": 365
                },
                "Confidence": 0.91490805149078,
                "BodyAttributeInfo": {
                    "UpperBodyCloth": {
                        "Color": {
                            "Type": "xx",
                            "Probability": 0.0
                        },
                        "Sleeve": {
                            "Type": "xx",
                            "Probability": 0.0
                        },
                        "Texture": {
                            "Type": "xx",
                            "Probability": 0.0
                        }
                    },
                    "Orientation": {
                        "Type": "xx",
                        "Probability": 0.0
                    },
                    "LowerBodyCloth": {
                        "Color": {
                            "Type": "xx",
                            "Probability": 0.0
                        },
                        "Length": {
                            "Type": "xx",
                            "Probability": 0.0
                        },
                        "Type": {
                            "Type": "xx",
                            "Probability": 0.0
                        }
                    },
                    "Gender": {
                        "Type": "xx",
                        "Probability": 0.0
                    },
                    "Age": {
                        "Type": "xx",
                        "Probability": 0.0
                    },
                    "Bag": {
                        "Type": "xx",
                        "Probability": 0.0
                    }
                }
            }
        ],
        "BodyModelVersion": "1.0",
        "RequestId": "13ce6864-614a-4a9f-8207-c68fc9c552c4"
    }
}
```

