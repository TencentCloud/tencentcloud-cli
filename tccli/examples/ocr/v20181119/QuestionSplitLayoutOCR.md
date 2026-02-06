**Example 1: 试卷切题**

试卷切题

Input: 

```
tccli ocr QuestionSplitLayoutOCR --cli-unfold-argument  \
    --ImageUrl https://qq.com/1.jpg
```

Output: 
```
{
    "Response": {
        "QuestionInfo": [
            {
                "Angle": 0,
                "Height": 3368,
                "ImageBase64": "",
                "OrgHeight": 3368,
                "OrgWidth": 2188,
                "ResultList": [
                    {
                        "Answer": [],
                        "Coord": [
                            {
                                "LeftBottom": {
                                    "X": 197,
                                    "Y": 1508
                                },
                                "LeftTop": {
                                    "X": 197,
                                    "Y": 568
                                },
                                "RightBottom": {
                                    "X": 2019,
                                    "Y": 1508
                                },
                                "RightTop": {
                                    "X": 2019,
                                    "Y": 568
                                }
                            }
                        ],
                        "Figure": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 197,
                                        "Y": 1066
                                    },
                                    "LeftTop": {
                                        "X": 197,
                                        "Y": 568
                                    },
                                    "RightBottom": {
                                        "X": 2019,
                                        "Y": 1066
                                    },
                                    "RightTop": {
                                        "X": 2019,
                                        "Y": 568
                                    }
                                },
                                "GroupType": "fill-in-the-blank",
                                "Index": 0,
                                "ResultList": null,
                                "Text": ""
                            }
                        ],
                        "Option": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 275,
                                        "Y": 1230
                                    },
                                    "LeftTop": {
                                        "X": 275,
                                        "Y": 1169
                                    },
                                    "RightBottom": {
                                        "X": 595,
                                        "Y": 1230
                                    },
                                    "RightTop": {
                                        "X": 595,
                                        "Y": 1169
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 2,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 729,
                                        "Y": 1232
                                    },
                                    "LeftTop": {
                                        "X": 729,
                                        "Y": 1174
                                    },
                                    "RightBottom": {
                                        "X": 1083,
                                        "Y": 1232
                                    },
                                    "RightTop": {
                                        "X": 1083,
                                        "Y": 1174
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 3,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 1218,
                                        "Y": 1230
                                    },
                                    "LeftTop": {
                                        "X": 1218,
                                        "Y": 1172
                                    },
                                    "RightBottom": {
                                        "X": 1564,
                                        "Y": 1230
                                    },
                                    "RightTop": {
                                        "X": 1564,
                                        "Y": 1172
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 4,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 1696,
                                        "Y": 1229
                                    },
                                    "LeftTop": {
                                        "X": 1696,
                                        "Y": 1169
                                    },
                                    "RightBottom": {
                                        "X": 2002,
                                        "Y": 1229
                                    },
                                    "RightTop": {
                                        "X": 2002,
                                        "Y": 1169
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 5,
                                "ResultList": null,
                                "Text": ""
                            }
                        ],
                        "Parse": [],
                        "Question": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 200,
                                        "Y": 1148
                                    },
                                    "LeftTop": {
                                        "X": 200,
                                        "Y": 1073
                                    },
                                    "RightBottom": {
                                        "X": 1761,
                                        "Y": 1148
                                    },
                                    "RightTop": {
                                        "X": 1761,
                                        "Y": 1073
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 1,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 200,
                                        "Y": 1508
                                    },
                                    "LeftTop": {
                                        "X": 200,
                                        "Y": 1239
                                    },
                                    "RightBottom": {
                                        "X": 2019,
                                        "Y": 1508
                                    },
                                    "RightTop": {
                                        "X": 2019,
                                        "Y": 1239
                                    }
                                },
                                "GroupType": "fill-in-the-blank",
                                "Index": 6,
                                "ResultList": null,
                                "Text": ""
                            }
                        ],
                        "Table": []
                    },
                    {
                        "Answer": [],
                        "Coord": [
                            {
                                "LeftBottom": {
                                    "X": 111,
                                    "Y": 3284
                                },
                                "LeftTop": {
                                    "X": 111,
                                    "Y": 1615
                                },
                                "RightBottom": {
                                    "X": 2030,
                                    "Y": 3284
                                },
                                "RightTop": {
                                    "X": 2030,
                                    "Y": 1615
                                }
                            }
                        ],
                        "Figure": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 1615,
                                        "Y": 2490
                                    },
                                    "LeftTop": {
                                        "X": 1615,
                                        "Y": 2232
                                    },
                                    "RightBottom": {
                                        "X": 2030,
                                        "Y": 2490
                                    },
                                    "RightTop": {
                                        "X": 2030,
                                        "Y": 2232
                                    }
                                },
                                "GroupType": "problem-solving",
                                "Index": 13,
                                "ResultList": null,
                                "Text": ""
                            }
                        ],
                        "Option": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 267,
                                        "Y": 2120
                                    },
                                    "LeftTop": {
                                        "X": 267,
                                        "Y": 2047
                                    },
                                    "RightBottom": {
                                        "X": 902,
                                        "Y": 2120
                                    },
                                    "RightTop": {
                                        "X": 902,
                                        "Y": 2047
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 9,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 1133,
                                        "Y": 2119
                                    },
                                    "LeftTop": {
                                        "X": 1133,
                                        "Y": 2060
                                    },
                                    "RightBottom": {
                                        "X": 1963,
                                        "Y": 2119
                                    },
                                    "RightTop": {
                                        "X": 1963,
                                        "Y": 2060
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 10,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 260,
                                        "Y": 2209
                                    },
                                    "LeftTop": {
                                        "X": 260,
                                        "Y": 2136
                                    },
                                    "RightBottom": {
                                        "X": 1085,
                                        "Y": 2209
                                    },
                                    "RightTop": {
                                        "X": 1085,
                                        "Y": 2136
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 11,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 1133,
                                        "Y": 2207
                                    },
                                    "LeftTop": {
                                        "X": 1133,
                                        "Y": 2151
                                    },
                                    "RightBottom": {
                                        "X": 1918,
                                        "Y": 2207
                                    },
                                    "RightTop": {
                                        "X": 1918,
                                        "Y": 2151
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 12,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 258,
                                        "Y": 2834
                                    },
                                    "LeftTop": {
                                        "X": 258,
                                        "Y": 2771
                                    },
                                    "RightBottom": {
                                        "X": 1746,
                                        "Y": 2834
                                    },
                                    "RightTop": {
                                        "X": 1746,
                                        "Y": 2771
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 15,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 258,
                                        "Y": 2927
                                    },
                                    "LeftTop": {
                                        "X": 258,
                                        "Y": 2861
                                    },
                                    "RightBottom": {
                                        "X": 1300,
                                        "Y": 2927
                                    },
                                    "RightTop": {
                                        "X": 1300,
                                        "Y": 2861
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 16,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 258,
                                        "Y": 3013
                                    },
                                    "LeftTop": {
                                        "X": 258,
                                        "Y": 2950
                                    },
                                    "RightBottom": {
                                        "X": 1973,
                                        "Y": 3013
                                    },
                                    "RightTop": {
                                        "X": 1973,
                                        "Y": 2950
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 17,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 251,
                                        "Y": 3101
                                    },
                                    "LeftTop": {
                                        "X": 251,
                                        "Y": 3039
                                    },
                                    "RightBottom": {
                                        "X": 1725,
                                        "Y": 3101
                                    },
                                    "RightTop": {
                                        "X": 1725,
                                        "Y": 3039
                                    }
                                },
                                "GroupType": "multiple-choice",
                                "Index": 18,
                                "ResultList": null,
                                "Text": ""
                            }
                        ],
                        "Parse": [],
                        "Question": [
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 123,
                                        "Y": 1682
                                    },
                                    "LeftTop": {
                                        "X": 123,
                                        "Y": 1615
                                    },
                                    "RightBottom": {
                                        "X": 1649,
                                        "Y": 1682
                                    },
                                    "RightTop": {
                                        "X": 1649,
                                        "Y": 1615
                                    }
                                },
                                "GroupType": "problem-solving",
                                "Index": 7,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 123,
                                        "Y": 2300
                                    },
                                    "LeftTop": {
                                        "X": 123,
                                        "Y": 1694
                                    },
                                    "RightBottom": {
                                        "X": 1948,
                                        "Y": 2300
                                    },
                                    "RightTop": {
                                        "X": 1948,
                                        "Y": 1694
                                    }
                                },
                                "GroupType": "problem-solving",
                                "Index": 8,
                                "ResultList": null,
                                "Text": ""
                            },
                            {
                                "Coord": {
                                    "LeftBottom": {
                                        "X": 111,
                                        "Y": 3284
                                    },
                                    "LeftTop": {
                                        "X": 111,
                                        "Y": 2500
                                    },
                                    "RightBottom": {
                                        "X": 2026,
                                        "Y": 3284
                                    },
                                    "RightTop": {
                                        "X": 2026,
                                        "Y": 2500
                                    }
                                },
                                "GroupType": "problem-solving",
                                "Index": 14,
                                "ResultList": null,
                                "Text": ""
                            }
                        ],
                        "Table": []
                    }
                ],
                "Width": 2188
            }
        ],
        "RequestId": "7a534f1d-2bb1-4e87-b79a-f8d37d6ab265"
    }
}
```

