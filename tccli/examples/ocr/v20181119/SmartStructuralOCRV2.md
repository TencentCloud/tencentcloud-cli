**Example 1: 智能结构化识别V2**

智能结构化识别新接口

Input: 

```
tccli ocr SmartStructuralOCRV2 --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/SmartStructuralOCR/SmartStructuralOCRV2.jpg
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "StructuralList": [
            {
                "Groups": [
                    {
                        "Lines": [
                            {
                                "Key": {
                                    "AutoName": "abc"
                                },
                                "Value": {
                                    "AutoContent": "abc",
                                    "Coord": {
                                        "LeftTop": {
                                            "X": 0,
                                            "Y": 0
                                        },
                                        "RightTop": {
                                            "X": 0,
                                            "Y": 0
                                        },
                                        "RightBottom": {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        ],
        "WordList": [
            {
                "DetectedText": "abc",
                "Coord": {}
            }
        ],
        "RequestId": "abc"
    }
}
```

