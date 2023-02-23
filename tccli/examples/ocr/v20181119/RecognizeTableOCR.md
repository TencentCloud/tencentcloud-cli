**Example 1: 表格识别示例代码**

表格识别示例代码

Input: 

```
tccli ocr RecognizeTableOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/TableOCR/TableOCR2.jpg \
    --IsPdf false
```

Output: 
```
{
    "Response": {
        "TableDetections": [
            {
                "Titles": null,
                "Cells": [
                    {
                        "ColTl": 0,
                        "RowTl": 0,
                        "ColBr": 9,
                        "RowBr": 1,
                        "Text": "五(1) 班卫生值日表",
                        "Type": "body",
                        "Confidence": 99.982088804245,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 25
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 193
                            },
                            {
                                "X": 774,
                                "Y": 193
                            },
                            {
                                "X": 774,
                                "Y": 282
                            },
                            {
                                "X": 26,
                                "Y": 282
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 0,
                        "RowTl": 1,
                        "ColBr": 1,
                        "RowBr": 2,
                        "Text": "星期一",
                        "Type": "body",
                        "Confidence": 99.96871948242188,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 282
                            },
                            {
                                "X": 107,
                                "Y": 282
                            },
                            {
                                "X": 107,
                                "Y": 326
                            },
                            {
                                "X": 26,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 1,
                        "RowTl": 1,
                        "ColBr": 2,
                        "RowBr": 2,
                        "Text": "梅亚婷",
                        "Type": "body",
                        "Confidence": 99.99997615814209,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 107,
                                "Y": 282
                            },
                            {
                                "X": 191,
                                "Y": 282
                            },
                            {
                                "X": 191,
                                "Y": 326
                            },
                            {
                                "X": 107,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 2,
                        "RowTl": 1,
                        "ColBr": 3,
                        "RowBr": 2,
                        "Text": "潘林峰",
                        "Type": "body",
                        "Confidence": 99.99949336051941,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 191,
                                "Y": 282
                            },
                            {
                                "X": 275,
                                "Y": 282
                            },
                            {
                                "X": 275,
                                "Y": 326
                            },
                            {
                                "X": 191,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 3,
                        "RowTl": 1,
                        "ColBr": 4,
                        "RowBr": 2,
                        "Text": "余校凯",
                        "Type": "body",
                        "Confidence": 99.98820424079895,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 275,
                                "Y": 282
                            },
                            {
                                "X": 359,
                                "Y": 282
                            },
                            {
                                "X": 359,
                                "Y": 326
                            },
                            {
                                "X": 275,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 4,
                        "RowTl": 1,
                        "ColBr": 5,
                        "RowBr": 2,
                        "Text": "郑江豪",
                        "Type": "body",
                        "Confidence": 99.99780654907227,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 359,
                                "Y": 282
                            },
                            {
                                "X": 442,
                                "Y": 282
                            },
                            {
                                "X": 442,
                                "Y": 326
                            },
                            {
                                "X": 359,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 5,
                        "RowTl": 1,
                        "ColBr": 6,
                        "RowBr": 2,
                        "Text": "范立新",
                        "Type": "body",
                        "Confidence": 100,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 442,
                                "Y": 282
                            },
                            {
                                "X": 526,
                                "Y": 282
                            },
                            {
                                "X": 526,
                                "Y": 326
                            },
                            {
                                "X": 442,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 6,
                        "RowTl": 1,
                        "ColBr": 7,
                        "RowBr": 2,
                        "Text": "柯志生",
                        "Type": "body",
                        "Confidence": 99.99997019767761,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 526,
                                "Y": 282
                            },
                            {
                                "X": 610,
                                "Y": 282
                            },
                            {
                                "X": 610,
                                "Y": 326
                            },
                            {
                                "X": 526,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 7,
                        "RowTl": 1,
                        "ColBr": 8,
                        "RowBr": 2,
                        "Text": "周于",
                        "Type": "body",
                        "Confidence": 99.9976396560669,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 610,
                                "Y": 282
                            },
                            {
                                "X": 694,
                                "Y": 282
                            },
                            {
                                "X": 694,
                                "Y": 326
                            },
                            {
                                "X": 610,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 8,
                        "RowTl": 1,
                        "ColBr": 9,
                        "RowBr": 2,
                        "Text": "李慧得",
                        "Type": "body",
                        "Confidence": 99.99997019767761,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 694,
                                "Y": 282
                            },
                            {
                                "X": 774,
                                "Y": 282
                            },
                            {
                                "X": 774,
                                "Y": 326
                            },
                            {
                                "X": 694,
                                "Y": 326
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 0,
                        "RowTl": 2,
                        "ColBr": 1,
                        "RowBr": 3,
                        "Text": "星期二",
                        "Type": "body",
                        "Confidence": 99.99971389770508,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 326
                            },
                            {
                                "X": 107,
                                "Y": 326
                            },
                            {
                                "X": 107,
                                "Y": 373
                            },
                            {
                                "X": 26,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 1,
                        "RowTl": 2,
                        "ColBr": 2,
                        "RowBr": 3,
                        "Text": "郑江尧",
                        "Type": "body",
                        "Confidence": 99.99954104423523,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 107,
                                "Y": 326
                            },
                            {
                                "X": 191,
                                "Y": 326
                            },
                            {
                                "X": 191,
                                "Y": 373
                            },
                            {
                                "X": 107,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 2,
                        "RowTl": 2,
                        "ColBr": 3,
                        "RowBr": 3,
                        "Text": "郑锦证",
                        "Type": "body",
                        "Confidence": 99.99963641166687,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 191,
                                "Y": 326
                            },
                            {
                                "X": 275,
                                "Y": 326
                            },
                            {
                                "X": 275,
                                "Y": 373
                            },
                            {
                                "X": 191,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 3,
                        "RowTl": 2,
                        "ColBr": 4,
                        "RowBr": 3,
                        "Text": "虞志峰",
                        "Type": "body",
                        "Confidence": 99.98536109924316,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 275,
                                "Y": 326
                            },
                            {
                                "X": 359,
                                "Y": 326
                            },
                            {
                                "X": 359,
                                "Y": 373
                            },
                            {
                                "X": 275,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 4,
                        "RowTl": 2,
                        "ColBr": 5,
                        "RowBr": 3,
                        "Text": "虞雨清",
                        "Type": "body",
                        "Confidence": 98.66757988929749,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 359,
                                "Y": 326
                            },
                            {
                                "X": 442,
                                "Y": 326
                            },
                            {
                                "X": 442,
                                "Y": 373
                            },
                            {
                                "X": 359,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 5,
                        "RowTl": 2,
                        "ColBr": 6,
                        "RowBr": 3,
                        "Text": "郑小伟",
                        "Type": "body",
                        "Confidence": 100,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 442,
                                "Y": 326
                            },
                            {
                                "X": 526,
                                "Y": 326
                            },
                            {
                                "X": 526,
                                "Y": 373
                            },
                            {
                                "X": 442,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 6,
                        "RowTl": 2,
                        "ColBr": 7,
                        "RowBr": 3,
                        "Text": "桂堂豪",
                        "Type": "body",
                        "Confidence": 99.99939799308777,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 526,
                                "Y": 326
                            },
                            {
                                "X": 610,
                                "Y": 326
                            },
                            {
                                "X": 610,
                                "Y": 373
                            },
                            {
                                "X": 526,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 7,
                        "RowTl": 2,
                        "ColBr": 8,
                        "RowBr": 3,
                        "Text": "何志勇",
                        "Type": "body",
                        "Confidence": 99.99999403953552,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 610,
                                "Y": 326
                            },
                            {
                                "X": 694,
                                "Y": 326
                            },
                            {
                                "X": 694,
                                "Y": 373
                            },
                            {
                                "X": 610,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 8,
                        "RowTl": 2,
                        "ColBr": 9,
                        "RowBr": 3,
                        "Text": "张志霞",
                        "Type": "body",
                        "Confidence": 99.99999403953552,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 694,
                                "Y": 326
                            },
                            {
                                "X": 774,
                                "Y": 326
                            },
                            {
                                "X": 774,
                                "Y": 373
                            },
                            {
                                "X": 694,
                                "Y": 373
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 0,
                        "RowTl": 3,
                        "ColBr": 1,
                        "RowBr": 4,
                        "Text": "星期三",
                        "Type": "body",
                        "Confidence": 99.99997019767761,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 373
                            },
                            {
                                "X": 107,
                                "Y": 373
                            },
                            {
                                "X": 107,
                                "Y": 418
                            },
                            {
                                "X": 26,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 1,
                        "RowTl": 3,
                        "ColBr": 2,
                        "RowBr": 4,
                        "Text": "桂小敏",
                        "Type": "body",
                        "Confidence": 99.99976754188538,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 107,
                                "Y": 373
                            },
                            {
                                "X": 191,
                                "Y": 373
                            },
                            {
                                "X": 191,
                                "Y": 418
                            },
                            {
                                "X": 107,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 2,
                        "RowTl": 3,
                        "ColBr": 3,
                        "RowBr": 4,
                        "Text": "雷玉婷",
                        "Type": "body",
                        "Confidence": 99.99997019767761,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 191,
                                "Y": 373
                            },
                            {
                                "X": 275,
                                "Y": 373
                            },
                            {
                                "X": 275,
                                "Y": 418
                            },
                            {
                                "X": 191,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 3,
                        "RowTl": 3,
                        "ColBr": 4,
                        "RowBr": 4,
                        "Text": "李洁",
                        "Type": "body",
                        "Confidence": 99.9998688697815,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 275,
                                "Y": 373
                            },
                            {
                                "X": 359,
                                "Y": 373
                            },
                            {
                                "X": 359,
                                "Y": 418
                            },
                            {
                                "X": 275,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 4,
                        "RowTl": 3,
                        "ColBr": 5,
                        "RowBr": 4,
                        "Text": "雷可丽",
                        "Type": "body",
                        "Confidence": 99.99987483024597,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 359,
                                "Y": 373
                            },
                            {
                                "X": 442,
                                "Y": 373
                            },
                            {
                                "X": 442,
                                "Y": 418
                            },
                            {
                                "X": 359,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 5,
                        "RowTl": 3,
                        "ColBr": 6,
                        "RowBr": 4,
                        "Text": "李爱兰",
                        "Type": "body",
                        "Confidence": 99.99998211860657,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 442,
                                "Y": 373
                            },
                            {
                                "X": 526,
                                "Y": 373
                            },
                            {
                                "X": 526,
                                "Y": 418
                            },
                            {
                                "X": 442,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 6,
                        "RowTl": 3,
                        "ColBr": 7,
                        "RowBr": 4,
                        "Text": "桂喻霞",
                        "Type": "body",
                        "Confidence": 99.99707341194153,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 526,
                                "Y": 373
                            },
                            {
                                "X": 610,
                                "Y": 373
                            },
                            {
                                "X": 610,
                                "Y": 418
                            },
                            {
                                "X": 526,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 7,
                        "RowTl": 3,
                        "ColBr": 8,
                        "RowBr": 4,
                        "Text": "郭培润",
                        "Type": "body",
                        "Confidence": 99.99442100524902,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 610,
                                "Y": 373
                            },
                            {
                                "X": 694,
                                "Y": 373
                            },
                            {
                                "X": 694,
                                "Y": 418
                            },
                            {
                                "X": 610,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 8,
                        "RowTl": 3,
                        "ColBr": 9,
                        "RowBr": 4,
                        "Text": "范亚妮",
                        "Type": "body",
                        "Confidence": 99.99880194664001,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 694,
                                "Y": 373
                            },
                            {
                                "X": 774,
                                "Y": 373
                            },
                            {
                                "X": 774,
                                "Y": 418
                            },
                            {
                                "X": 694,
                                "Y": 418
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 0,
                        "RowTl": 4,
                        "ColBr": 1,
                        "RowBr": 5,
                        "Text": "星期四",
                        "Type": "body",
                        "Confidence": 99.99974370002747,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 418
                            },
                            {
                                "X": 107,
                                "Y": 418
                            },
                            {
                                "X": 107,
                                "Y": 464
                            },
                            {
                                "X": 26,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 1,
                        "RowTl": 4,
                        "ColBr": 2,
                        "RowBr": 5,
                        "Text": "桂宗宙",
                        "Type": "body",
                        "Confidence": 99.99898076057434,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 107,
                                "Y": 418
                            },
                            {
                                "X": 191,
                                "Y": 418
                            },
                            {
                                "X": 191,
                                "Y": 464
                            },
                            {
                                "X": 107,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 2,
                        "RowTl": 4,
                        "ColBr": 3,
                        "RowBr": 5,
                        "Text": "李谓志",
                        "Type": "body",
                        "Confidence": 99.9998390674591,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 191,
                                "Y": 418
                            },
                            {
                                "X": 275,
                                "Y": 418
                            },
                            {
                                "X": 275,
                                "Y": 464
                            },
                            {
                                "X": 191,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 3,
                        "RowTl": 4,
                        "ColBr": 4,
                        "RowBr": 5,
                        "Text": "雷彩霞",
                        "Type": "body",
                        "Confidence": 99.99995231628418,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 275,
                                "Y": 418
                            },
                            {
                                "X": 359,
                                "Y": 418
                            },
                            {
                                "X": 359,
                                "Y": 464
                            },
                            {
                                "X": 275,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 4,
                        "RowTl": 4,
                        "ColBr": 5,
                        "RowBr": 5,
                        "Text": "郑佳勇",
                        "Type": "body",
                        "Confidence": 99.99539256095886,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 359,
                                "Y": 418
                            },
                            {
                                "X": 442,
                                "Y": 418
                            },
                            {
                                "X": 442,
                                "Y": 464
                            },
                            {
                                "X": 359,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 5,
                        "RowTl": 4,
                        "ColBr": 6,
                        "RowBr": 5,
                        "Text": "马佳辉",
                        "Type": "body",
                        "Confidence": 99.99973773956299,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 442,
                                "Y": 418
                            },
                            {
                                "X": 526,
                                "Y": 418
                            },
                            {
                                "X": 526,
                                "Y": 464
                            },
                            {
                                "X": 442,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 6,
                        "RowTl": 4,
                        "ColBr": 7,
                        "RowBr": 5,
                        "Text": "郭培建",
                        "Type": "body",
                        "Confidence": 99.99993443489075,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 526,
                                "Y": 418
                            },
                            {
                                "X": 610,
                                "Y": 418
                            },
                            {
                                "X": 610,
                                "Y": 464
                            },
                            {
                                "X": 526,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 7,
                        "RowTl": 4,
                        "ColBr": 8,
                        "RowBr": 5,
                        "Text": "李智政",
                        "Type": "body",
                        "Confidence": 99.99950528144836,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 610,
                                "Y": 418
                            },
                            {
                                "X": 694,
                                "Y": 418
                            },
                            {
                                "X": 694,
                                "Y": 464
                            },
                            {
                                "X": 610,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 8,
                        "RowTl": 4,
                        "ColBr": 9,
                        "RowBr": 5,
                        "Text": "范成龙",
                        "Type": "body",
                        "Confidence": 100,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 694,
                                "Y": 418
                            },
                            {
                                "X": 774,
                                "Y": 418
                            },
                            {
                                "X": 774,
                                "Y": 464
                            },
                            {
                                "X": 694,
                                "Y": 464
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 0,
                        "RowTl": 5,
                        "ColBr": 1,
                        "RowBr": 6,
                        "Text": "星期五",
                        "Type": "body",
                        "Confidence": 99.99926090240479,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 464
                            },
                            {
                                "X": 107,
                                "Y": 464
                            },
                            {
                                "X": 107,
                                "Y": 510
                            },
                            {
                                "X": 26,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 1,
                        "RowTl": 5,
                        "ColBr": 2,
                        "RowBr": 6,
                        "Text": "朱凯鹏",
                        "Type": "body",
                        "Confidence": 99.99980926513672,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 107,
                                "Y": 464
                            },
                            {
                                "X": 191,
                                "Y": 464
                            },
                            {
                                "X": 191,
                                "Y": 510
                            },
                            {
                                "X": 107,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 2,
                        "RowTl": 5,
                        "ColBr": 3,
                        "RowBr": 6,
                        "Text": "虞校水",
                        "Type": "body",
                        "Confidence": 99.98979568481445,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 191,
                                "Y": 464
                            },
                            {
                                "X": 275,
                                "Y": 464
                            },
                            {
                                "X": 275,
                                "Y": 510
                            },
                            {
                                "X": 191,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 3,
                        "RowTl": 5,
                        "ColBr": 4,
                        "RowBr": 6,
                        "Text": "郑雯丽",
                        "Type": "body",
                        "Confidence": 99.99974370002747,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 275,
                                "Y": 464
                            },
                            {
                                "X": 359,
                                "Y": 464
                            },
                            {
                                "X": 359,
                                "Y": 510
                            },
                            {
                                "X": 275,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 4,
                        "RowTl": 5,
                        "ColBr": 5,
                        "RowBr": 6,
                        "Text": "郑琳",
                        "Type": "body",
                        "Confidence": 100,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 14
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 359,
                                "Y": 464
                            },
                            {
                                "X": 442,
                                "Y": 464
                            },
                            {
                                "X": 442,
                                "Y": 510
                            },
                            {
                                "X": 359,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 5,
                        "RowTl": 5,
                        "ColBr": 6,
                        "RowBr": 6,
                        "Text": "范越",
                        "Type": "body",
                        "Confidence": 99.99940991401672,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 442,
                                "Y": 464
                            },
                            {
                                "X": 526,
                                "Y": 464
                            },
                            {
                                "X": 526,
                                "Y": 510
                            },
                            {
                                "X": 442,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 6,
                        "RowTl": 5,
                        "ColBr": 7,
                        "RowBr": 6,
                        "Text": "张鑫涛",
                        "Type": "body",
                        "Confidence": 99.99998211860657,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 526,
                                "Y": 464
                            },
                            {
                                "X": 610,
                                "Y": 464
                            },
                            {
                                "X": 610,
                                "Y": 510
                            },
                            {
                                "X": 526,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 7,
                        "RowTl": 5,
                        "ColBr": 8,
                        "RowBr": 6,
                        "Text": "雷万林",
                        "Type": "body",
                        "Confidence": 99.99470114707947,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 610,
                                "Y": 464
                            },
                            {
                                "X": 694,
                                "Y": 464
                            },
                            {
                                "X": 694,
                                "Y": 511
                            },
                            {
                                "X": 610,
                                "Y": 510
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 8,
                        "RowTl": 5,
                        "ColBr": 9,
                        "RowBr": 6,
                        "Text": "雷建国",
                        "Type": "body",
                        "Confidence": 100,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 15
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 694,
                                "Y": 464
                            },
                            {
                                "X": 774,
                                "Y": 464
                            },
                            {
                                "X": 774,
                                "Y": 510
                            },
                            {
                                "X": 694,
                                "Y": 511
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 0,
                        "RowTl": 6,
                        "ColBr": 9,
                        "RowBr": 7,
                        "Text": "备注:李林涛、梅美雪、江瑶洁、郑佳杰、李建华负责黑板及窗台等区域卫生。",
                        "Type": "body",
                        "Confidence": 99.58259463310242,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 17
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 510
                            },
                            {
                                "X": 774,
                                "Y": 510
                            },
                            {
                                "X": 774,
                                "Y": 557
                            },
                            {
                                "X": 26,
                                "Y": 557
                            }
                        ],
                        "AdvancedInfo": ""
                    },
                    {
                        "ColTl": 0,
                        "RowTl": 7,
                        "ColBr": 9,
                        "RowBr": 8,
                        "Text": "我们在一起一直在努力!",
                        "Type": "body",
                        "Confidence": 98.30002188682556,
                        "Contents": [
                            {
                                "ParagNo": 0,
                                "WordSize": 22
                            }
                        ],
                        "Polygon": [
                            {
                                "X": 26,
                                "Y": 557
                            },
                            {
                                "X": 774,
                                "Y": 557
                            },
                            {
                                "X": 774,
                                "Y": 604
                            },
                            {
                                "X": 26,
                                "Y": 604
                            }
                        ],
                        "AdvancedInfo": ""
                    }
                ],
                "Type": 1,
                "TableCoordPoint": [
                    {
                        "X": 26,
                        "Y": 193
                    },
                    {
                        "X": 774,
                        "Y": 193
                    },
                    {
                        "X": 774,
                        "Y": 604
                    },
                    {
                        "X": 26,
                        "Y": 604
                    }
                ]
            }
        ],
        "PdfPageSize": 0,
        "Data": "UEsDBBQAAAAIAAAAAADO8yasOQEAAKsEAAATAAAAW0NvbnRlbnRfVHlwZXNdLnhtbK2Uy27CMBBF93xFlG1FTLvoogI2bbctUvsDrj1JXPySZ6Dw952ERwUqBBQ2saLxveeOPfL4cx0Bs5WzHid5TRSfhEBVg5NYhAieK2VIThL/pkpEqeayAvEwGj0KFTyBpyE1Hvl0kGXjFyjlwlL2uuIKmuAn+XeEKs+eN3sb3CQ3rvFoC+KUjMFHKhmjNUoSl0VTPSlNYPGMdun1UWvDbVsFK9s9WJuId3+Q9yWkZDRkM5noTTp2FCsrsJYJ9Acl4ysszif+hxrK0ijQQS0cSwqMCaTGGoCcLQ68L4hCaws3z9CadsOJ5wU23/veE==",
        "Angle": 0,
        "RequestId": "aab831e6-7ae6-49bd-b599-af3e39052364"
    }
}
```

