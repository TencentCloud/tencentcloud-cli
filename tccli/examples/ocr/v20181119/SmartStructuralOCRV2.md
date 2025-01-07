**Example 1: 智能结构化识别V2**

智能结构化识别新接口

Input: 

```
tccli ocr SmartStructuralOCRV2 --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/SmartStructuralOCR/SmartStructuralPro1.png \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q== \
    --IsPdf True \
    --PdfPageNumber 1 \
    --ItemNames 号码 \
    --ReturnFullText False \
    --ConfigId General
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
                                    "AutoName": "号码",
                                    "ConfigName": "number"
                                },
                                "Value": {
                                    "AutoContent": "176***101",
                                    "Coord": {
                                        "LeftTop": {
                                            "X": 0,
                                            "Y": 0
                                        },
                                        "LeftBottom": {
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
                "DetectedText": "ORD0****9",
                "Coord": {
                    "LeftTop": {
                        "X": 0,
                        "Y": 0
                    },
                    "LeftBottom": {
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
        ],
        "RequestId": "137****9"
    }
}
```

