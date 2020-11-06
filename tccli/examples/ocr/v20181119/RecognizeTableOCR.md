**Example 1: 表格识别示例代码**



Input: 

```
tccli ocr RecognizeTableOCR --cli-unfold-argument  \
    --ImageUrl xxx \
    --IsPdf false
```

Output: 
```
{
    "Response": {
        "TableDetections": [
            {
                "Titles": [],
                "Cells": [
                    {
                        "ColTl": -1,
                        "RowTl": -1,
                        "ColBr": -1,
                        "RowBr": -1,
                        "Text": "生产销售单11811",
                        "Type": "header",
                        "Confidence": 83.75851511955261,
                        "Contents": [
                            {
                                "ParagNo": 3,
                                "WordSize": 36
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 2615,
                                "Y": 183
                            },
                            {
                                "X": 2620,
                                "Y": 495
                            },
                            {
                                "X": 2576,
                                "Y": 496
                            },
                            {
                                "X": 2571,
                                "Y": 184
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": -1,
                        "RowTl": -1,
                        "ColBr": -1,
                        "RowBr": -1,
                        "Text": "用代码(必填)",
                        "Type": "header",
                        "Confidence": 91.66063666343689,
                        "Contents": [
                            {
                                "ParagNo": 3,
                                "WordSize": 36
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 2640,
                                "Y": 495
                            },
                            {
                                "X": 2644,
                                "Y": 705
                            },
                            {
                                "X": 2604,
                                "Y": 706
                            },
                            {
                                "X": 2600,
                                "Y": 496
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": -1,
                        "RowTl": -1,
                        "ColBr": -1,
                        "RowBr": -1,
                        "Text": "91441900598956858B",
                        "Type": "header",
                        "Confidence": 99.87912774085999,
                        "Contents": [
                            {
                                "ParagNo": 5,
                                "WordSize": 42
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 2622,
                                "Y": 745
                            },
                            {
                                "X": 2629,
                                "Y": 1145
                            },
                            {
                                "X": 2585,
                                "Y": 1146
                            },
                            {
                                "X": 2578,
                                "Y": 746
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": -1,
                        "RowTl": -1,
                        "ColBr": -1,
                        "RowBr": -1,
                        "Text": "监管方式(",
                        "Type": "header",
                        "Confidence": 99.95506405830383,
                        "Contents": [
                            {
                                "ParagNo": 11,
                                "WordSize": 37
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 2645,
                                "Y": 1394
                            },
                            {
                                "X": 2647,
                                "Y": 1563
                            },
                            {
                                "X": 2605,
                                "Y": 1564
                            },
                            {
                                "X": 2603,
                                "Y": 1395
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": -1,
                        "RowTl": -1,
                        "ColBr": -1,
                        "RowBr": -1,
                        "Text": "(必填)",
                        "Type": "header",
                        "Confidence": 93.90166997909546,
                        "Contents": [
                            {
                                "ParagNo": 11,
                                "WordSize": 37
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 2652,
                                "Y": 1547
                            },
                            {
                                "X": 2654,
                                "Y": 1644
                            },
                            {
                                "X": 2610,
                                "Y": 1645
                            },
                            {
                                "X": 2608,
                                "Y": 1548
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": -1,
                        "RowTl": -1,
                        "ColBr": -1,
                        "RowBr": -1,
                        "Text": "生产销售单位公司名(必填)",
                        "Type": "header",
                        "Confidence": 98.71867895126343,
                        "Contents": [
                            {
                                "ParagNo": 3,
                                "WordSize": 36
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 2525,
                                "Y": 184
                            },
                            {
                                "X": 2532,
                                "Y": 594
                            },
                            {
                                "X": 2491,
                                "Y": 595
                            },
                            {
                                "X": 2484,
                                "Y": 185
                            }
                        ],
                        "AdvancedInfo": ""
                    }
                ]
            },
            {
                "Titles": [
                    {
                        "Text": "征免性质(必填)"
                    }
                ],
                "Cells": [
                    {
                        "ColTl": 0,
                        "RowTl": 0,
                        "ColBr": 2,
                        "RowBr": 1,
                        "Text": "",
                        "Type": "body",
                        "Confidence": 0,
                        "Contents": [],
                        "Polygon": [
                            {
                                "X": 2474,
                                "Y": 190
                            },
                            {
                                "X": 2484,
                                "Y": 755
                            },
                            {
                                "X": 2435,
                                "Y": 756
                            },
                            {
                                "X": 2429,
                                "Y": 191
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 10,
                        "RowTl": 12,
                        "ColBr": 11,
                        "RowBr": 13,
                        "Text": "中国",
                        "Type": "body",
                        "Confidence": 99.99748468399048,
                        "Contents": [
                            {
                                "ParagNo": 4,
                                "WordSize": 57
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 993,
                                "Y": 3183
                            },
                            {
                                "X": 995,
                                "Y": 3407
                            },
                            {
                                "X": 841,
                                "Y": 3409
                            },
                            {
                                "X": 838,
                                "Y": 3184
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 11,
                        "RowTl": 12,
                        "ColBr": 12,
                        "RowBr": 13,
                        "Text": "马来西亚",
                        "Type": "body",
                        "Confidence": 98.29457998275757,
                        "Contents": [
                            {
                                "ParagNo": 4,
                                "WordSize": 57
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 995,
                                "Y": 3407
                            },
                            {
                                "X": 998,
                                "Y": 3672
                            },
                            {
                                "X": 844,
                                "Y": 3673
                            },
                            {
                                "X": 841,
                                "Y": 3409
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 12,
                        "RowTl": 12,
                        "ColBr": 13,
                        "RowBr": 14,
                        "Text": "东 东亮",
                        "Type": "body",
                        "Confidence": 90.21790623664856,
                        "Contents": [
                            {
                                "ParagNo": 4,
                                "WordSize": 39
                            },
                            {
                                "ParagNo": 4,
                                "WordSize": 39
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 998,
                                "Y": 3672
                            },
                            {
                                "X": 1002,
                                "Y": 3923
                            },
                            {
                                "X": 692,
                                "Y": 3924
                            },
                            {
                                "X": 688,
                                "Y": 3675
                            }
                        ],
                        "AdvancedInfo": ""
                    }
                ]
            }
        ],
        "Data": "8HAABnHAAAFAAAAAAAAAAAAAAAAADMJAAAeGwvc2hhcmVkU3RyaW5ncy54bWxQSwECFAAUAAAACAAAAAAAcxSJldcBAAD9BQAADQAAAAAAAAAAAAAAAACtLAAAeGwvc3R5bGVzLnhtbFBLAQIUABQAAAAIAAAAAAC8TIYcSAYAAP4kAAATAAAAAAAAAAAAAAAAAK8uAAB4bC90aGVtZS90aGVtZTEueG1sUEsBAhQAFAAAAAgAAAAAANG5P9oECwAAUU0AABgAAAAAAAAAAAAAAAAAKDUAAHhsL3dvcmtzaGVldHMvc2hlZXQyLnhtbFBLAQIUABQAAAAIAAAAAADjsY7PqAMAAE8PAAAYAAAAAAAAAAAAAAAAAGJAAAB4bC93b3Jrc2hlZXRzL3NoZWV0MS54bWxQSwUGAAAAAAwADAALAwAAQEQAAAAA",
        "RequestId": "98f8fcbf-933a-4e95-ac48-6f1a9308fs53"
    }
}
```

