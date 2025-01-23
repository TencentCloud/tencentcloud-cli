**Example 1: 试题识别**



Input: 

```
tccli ocr QuestionOCR --cli-unfold-argument  \
    --ImageUrl https://qq.com/1.jpg
```

Output: 
```
{
    "Response": {
        "QuestionInfo": [
            {
                "Angle": -0.16999949956523785,
                "Height": 200,
                "ImageBase64": "4AAQSkZJRgABAQAAAQABAAD==",
                "OrgHeight": 196,
                "OrgWidth": 1626,
                "ResultList": [
                    {
                        "Answer": [],
                        "Figure": [],
                        "Option": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 65,
                                        "Y": 689
                                    },
                                    "LeftTop": {
                                        "X": 65,
                                        "Y": 650
                                    },
                                    "RightBottom": {
                                        "X": 234,
                                        "Y": 689
                                    },
                                    "RightTop": {
                                        "X": 234,
                                        "Y": 650
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 1,
                                "ResultList": null,
                                "Text": "A.b>c>a"
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 364,
                                        "Y": 689
                                    },
                                    "LeftTop": {
                                        "X": 364,
                                        "Y": 650
                                    },
                                    "RightBottom": {
                                        "X": 552,
                                        "Y": 689
                                    },
                                    "RightTop": {
                                        "X": 552,
                                        "Y": 650
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 2,
                                "ResultList": null,
                                "Text": "B.a>b>c"
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 700,
                                        "Y": 689
                                    },
                                    "LeftTop": {
                                        "X": 700,
                                        "Y": 650
                                    },
                                    "RightBottom": {
                                        "X": 871,
                                        "Y": 689
                                    },
                                    "RightTop": {
                                        "X": 871,
                                        "Y": 650
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 3,
                                "ResultList": null,
                                "Text": "C.c>a>b"
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 1037,
                                        "Y": 689
                                    },
                                    "LeftTop": {
                                        "X": 1037,
                                        "Y": 650
                                    },
                                    "RightBottom": {
                                        "X": 1214,
                                        "Y": 689
                                    },
                                    "RightTop": {
                                        "X": 1214,
                                        "Y": 650
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 4,
                                "ResultList": null,
                                "Text": "D.c>b>a"
                            }
                        ],
                        "Question": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 14,
                                        "Y": 845
                                    },
                                    "LeftTop": {
                                        "X": 14,
                                        "Y": 759
                                    },
                                    "RightBottom": {
                                        "X": 1603,
                                        "Y": 845
                                    },
                                    "RightTop": {
                                        "X": 1603,
                                        "Y": 759
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 0,
                                "ResultList": null,
                                "Text": "5.若M(-6,a),N(2,b),P(6,c)三点都在反比例函数$y=\\frac{m^{2}+1}{x}$图象上，则a、b、c的大小关系为()"
                            }
                        ],
                        "Table": []
                    }
                ],
                "Width": 1626
            }
        ],
        "RequestId": "644651c0-cae4-413b-a90a-fa0d3f79e009"
    }
}
```

