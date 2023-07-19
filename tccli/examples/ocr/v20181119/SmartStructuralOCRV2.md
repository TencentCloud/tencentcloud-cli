**Example 1: 智能结构化识别V2**

智能结构化识别新接口

Input: 

```
tccli ocr SmartStructuralOCRV2 --cli-unfold-argument  \
    --ImageUrl abc \
    --ImageBase64 abc \
    --IsPdf True \
    --PdfPageNumber 1 \
    --ItemNames abc \
    --ReturnFullText True \
    --ConfigId abc
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
                                    "AutoName": "abc",
                                    "ConfigName": "abc"
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

