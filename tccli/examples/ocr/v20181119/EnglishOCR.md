**Example 1: 英文识别示例代码**

英文识别示例代码

Input: 

```
tccli ocr EnglishOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "DetectedText": "No matter how long the",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 228,
                        "Y": 244
                    },
                    {
                        "X": 228,
                        "Y": 269
                    },
                    {
                        "X": 562,
                        "Y": 270
                    },
                    {
                        "X": 562,
                        "Y": 245
                    }
                ],
                "AdvancedInfo": "{}",
                "WordCoordPoint": [
                    {
                        "WordCoordinate": [
                            {
                                "X": 226,
                                "Y": 270
                            },
                            {
                                "X": 226,
                                "Y": 241
                            },
                            {
                                "X": 270,
                                "Y": 242
                            },
                            {
                                "X": 270,
                                "Y": 271
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 278,
                                "Y": 271
                            },
                            {
                                "X": 279,
                                "Y": 242
                            },
                            {
                                "X": 368,
                                "Y": 242
                            },
                            {
                                "X": 368,
                                "Y": 271
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 378,
                                "Y": 271
                            },
                            {
                                "X": 378,
                                "Y": 242
                            },
                            {
                                "X": 437,
                                "Y": 242
                            },
                            {
                                "X": 437,
                                "Y": 271
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 446,
                                "Y": 271
                            },
                            {
                                "X": 446,
                                "Y": 242
                            },
                            {
                                "X": 502,
                                "Y": 242
                            },
                            {
                                "X": 502,
                                "Y": 271
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 514,
                                "Y": 271
                            },
                            {
                                "X": 514,
                                "Y": 242
                            },
                            {
                                "X": 566,
                                "Y": 243
                            },
                            {
                                "X": 566,
                                "Y": 272
                            }
                        ]
                    }
                ],
                "CandWord": [
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "N"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "o"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "m"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "a"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "t"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "t"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "e"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "r"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "h"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "o"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "w"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "l"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "o"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "n"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "g"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "t"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "h"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "e"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    }
                ],
                "Words": [
                    {
                        "Confidence": 99,
                        "Character": "No"
                    },
                    {
                        "Confidence": 99,
                        "Character": "matter"
                    },
                    {
                        "Confidence": 99,
                        "Character": "how"
                    },
                    {
                        "Confidence": 99,
                        "Character": "long"
                    },
                    {
                        "Confidence": 99,
                        "Character": "the"
                    }
                ]
            },
            {
                "DetectedText": "night, the day will come.",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 226,
                        "Y": 303
                    },
                    {
                        "X": 226,
                        "Y": 331
                    },
                    {
                        "X": 569,
                        "Y": 331
                    },
                    {
                        "X": 569,
                        "Y": 303
                    }
                ],
                "AdvancedInfo": "{}",
                "WordCoordPoint": [
                    {
                        "WordCoordinate": [
                            {
                                "X": 224,
                                "Y": 333
                            },
                            {
                                "X": 224,
                                "Y": 301
                            },
                            {
                                "X": 297,
                                "Y": 301
                            },
                            {
                                "X": 297,
                                "Y": 333
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 298,
                                "Y": 333
                            },
                            {
                                "X": 298,
                                "Y": 301
                            },
                            {
                                "X": 305,
                                "Y": 301
                            },
                            {
                                "X": 305,
                                "Y": 333
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 316,
                                "Y": 333
                            },
                            {
                                "X": 316,
                                "Y": 301
                            },
                            {
                                "X": 352,
                                "Y": 301
                            },
                            {
                                "X": 352,
                                "Y": 333
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 365,
                                "Y": 333
                            },
                            {
                                "X": 365,
                                "Y": 301
                            },
                            {
                                "X": 423,
                                "Y": 300
                            },
                            {
                                "X": 423,
                                "Y": 333
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 432,
                                "Y": 333
                            },
                            {
                                "X": 432,
                                "Y": 300
                            },
                            {
                                "X": 474,
                                "Y": 300
                            },
                            {
                                "X": 474,
                                "Y": 332
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 483,
                                "Y": 332
                            },
                            {
                                "X": 483,
                                "Y": 300
                            },
                            {
                                "X": 565,
                                "Y": 300
                            },
                            {
                                "X": 565,
                                "Y": 332
                            }
                        ]
                    },
                    {
                        "WordCoordinate": [
                            {
                                "X": 567,
                                "Y": 332
                            },
                            {
                                "X": 567,
                                "Y": 300
                            },
                            {
                                "X": 591,
                                "Y": 300
                            },
                            {
                                "X": 591,
                                "Y": 332
                            }
                        ]
                    }
                ],
                "CandWord": [
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "n"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "i"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "g"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "h"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "t"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": ","
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "t"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "h"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "e"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "d"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "a"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "y"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "w"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "i"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "l"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "l"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "nil"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "c"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "o"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "m"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 100,
                                "Character": "e"
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    },
                    {
                        "CandWords": [
                            {
                                "Confidence": 99,
                                "Character": "."
                            },
                            {
                                "Confidence": 0,
                                "Character": "㊥"
                            }
                        ]
                    }
                ],
                "Words": [
                    {
                        "Confidence": 99,
                        "Character": "night"
                    },
                    {
                        "Confidence": 99,
                        "Character": ","
                    },
                    {
                        "Confidence": 99,
                        "Character": "the"
                    },
                    {
                        "Confidence": 99,
                        "Character": "day"
                    },
                    {
                        "Confidence": 99,
                        "Character": "will"
                    },
                    {
                        "Confidence": 99,
                        "Character": "come"
                    },
                    {
                        "Confidence": 99,
                        "Character": "."
                    }
                ]
            }
        ],
        "Angel": 0,
        "RequestId": "f2b87b6d-37c4-402f-b8b0-a74686f8f838"
    }
}
```

