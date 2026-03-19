**Example 1: 成功示例**



Input: 

```
tccli ocr SubmitQuestionMarkAgentJob --cli-unfold-argument  \
    --ImageBase64 None \
    --ImageUrl None \
    --PdfPageNumber None \
    --QuestionConfigMap None \
    --ReferenceAnswer None
```

Output: 
```
{
    "Response": {
        "JobId": "1410885500986064896",
        "QuestionInfo": [
            {
                "Angle": 0,
                "Height": 1532,
                "ImageBase64": "",
                "OrgHeight": 1532,
                "OrgWidth": 1154,
                "ResultList": [
                    {
                        "Answer": [],
                        "Coord": [
                            {
                                "LeftBottom": {
                                    "X": 113,
                                    "Y": 856
                                },
                                "LeftTop": {
                                    "X": 113,
                                    "Y": 351
                                },
                                "RightBottom": {
                                    "X": 576,
                                    "Y": 856
                                },
                                "RightTop": {
                                    "X": 576,
                                    "Y": 351
                                }
                            }
                        ],
                        "Figure": [],
                        "Option": [],
                        "Parse": [],
                        "Question": [],
                        "Table": []
                    },
                    {
                        "Answer": [],
                        "Coord": [
                            {
                                "LeftBottom": {
                                    "X": 117,
                                    "Y": 1354
                                },
                                "LeftTop": {
                                    "X": 117,
                                    "Y": 948
                                },
                                "RightBottom": {
                                    "X": 569,
                                    "Y": 1354
                                },
                                "RightTop": {
                                    "X": 569,
                                    "Y": 948
                                }
                            }
                        ],
                        "Figure": [],
                        "Option": [],
                        "Parse": [],
                        "Question": [],
                        "Table": []
                    },
                    {
                        "Answer": [],
                        "Coord": [
                            {
                                "LeftBottom": {
                                    "X": 595,
                                    "Y": 849
                                },
                                "LeftTop": {
                                    "X": 595,
                                    "Y": 282
                                },
                                "RightBottom": {
                                    "X": 1086,
                                    "Y": 849
                                },
                                "RightTop": {
                                    "X": 1086,
                                    "Y": 282
                                }
                            }
                        ],
                        "Figure": [],
                        "Option": [],
                        "Parse": [],
                        "Question": [],
                        "Table": []
                    },
                    {
                        "Answer": [],
                        "Coord": [
                            {
                                "LeftBottom": {
                                    "X": 595,
                                    "Y": 1344
                                },
                                "LeftTop": {
                                    "X": 595,
                                    "Y": 847
                                },
                                "RightBottom": {
                                    "X": 1047,
                                    "Y": 1344
                                },
                                "RightTop": {
                                    "X": 1047,
                                    "Y": 847
                                }
                            }
                        ],
                        "Figure": [],
                        "Option": [],
                        "Parse": [],
                        "Question": [],
                        "Table": []
                    }
                ],
                "Width": 1154
            }
        ],
        "RequestId": "ca2a3d55-3194-4e10-a125-67e12f7a7c32"
    }
}
```

