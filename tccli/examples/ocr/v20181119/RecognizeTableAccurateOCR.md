**Example 1: 表格识别示例代码**

表格识别示例代码

Input: 

```
tccli ocr RecognizeTableAccurateOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/TableOCRDDS/TableOCRDDS1.png
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "Data": "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",
        "PdfPageSize": 0,
        "RequestId": "f5a1fabb-956f-4622-9d5d-2982b01ac2ec",
        "TableDetections": [
            {
                "Cells": [
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 29
                            },
                            {
                                "X": 348,
                                "Y": 29
                            },
                            {
                                "X": 348,
                                "Y": 74
                            },
                            {
                                "X": 32,
                                "Y": 74
                            }
                        ],
                        "RowBr": 1,
                        "RowTl": 0,
                        "Text": "",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 29
                            },
                            {
                                "X": 574,
                                "Y": 29
                            },
                            {
                                "X": 574,
                                "Y": 74
                            },
                            {
                                "X": 348,
                                "Y": 74
                            }
                        ],
                        "RowBr": 1,
                        "RowTl": 0,
                        "Text": "本报告期末",
                        "Type": "body"
                    },
                    {
                        "ColBr": 4,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 574,
                                "Y": 29
                            },
                            {
                                "X": 872,
                                "Y": 29
                            },
                            {
                                "X": 873,
                                "Y": 74
                            },
                            {
                                "X": 574,
                                "Y": 74
                            }
                        ],
                        "RowBr": 1,
                        "RowTl": 0,
                        "Text": "期末余额",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 4,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 872,
                                "Y": 29
                            },
                            {
                                "X": 1166,
                                "Y": 29
                            },
                            {
                                "X": 1166,
                                "Y": 73
                            },
                            {
                                "X": 873,
                                "Y": 74
                            }
                        ],
                        "RowBr": 1,
                        "RowTl": 0,
                        "Text": "本报告期末比去年度末增减",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 74
                            },
                            {
                                "X": 348,
                                "Y": 74
                            },
                            {
                                "X": 348,
                                "Y": 106
                            },
                            {
                                "X": 32,
                                "Y": 106
                            }
                        ],
                        "RowBr": 2,
                        "RowTl": 1,
                        "Text": "总资产(元)",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 74
                            },
                            {
                                "X": 574,
                                "Y": 74
                            },
                            {
                                "X": 574,
                                "Y": 106
                            },
                            {
                                "X": 348,
                                "Y": 106
                            }
                        ],
                        "RowBr": 2,
                        "RowTl": 1,
                        "Text": "3,832,876,471.32",
                        "Type": "body"
                    },
                    {
                        "ColBr": 4,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 574,
                                "Y": 74
                            },
                            {
                                "X": 873,
                                "Y": 74
                            },
                            {
                                "X": 873,
                                "Y": 106
                            },
                            {
                                "X": 574,
                                "Y": 106
                            }
                        ],
                        "RowBr": 2,
                        "RowTl": 1,
                        "Text": "2,965,689,152.98",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 4,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 873,
                                "Y": 74
                            },
                            {
                                "X": 1166,
                                "Y": 73
                            },
                            {
                                "X": 1166,
                                "Y": 105
                            },
                            {
                                "X": 873,
                                "Y": 106
                            }
                        ],
                        "RowBr": 2,
                        "RowTl": 1,
                        "Text": "18.98%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 106
                            },
                            {
                                "X": 348,
                                "Y": 106
                            },
                            {
                                "X": 348,
                                "Y": 135
                            },
                            {
                                "X": 32,
                                "Y": 135
                            }
                        ],
                        "RowBr": 3,
                        "RowTl": 2,
                        "Text": "归属于上市公司股东的净资产",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 106
                            },
                            {
                                "X": 574,
                                "Y": 106
                            },
                            {
                                "X": 574,
                                "Y": 135
                            },
                            {
                                "X": 348,
                                "Y": 135
                            }
                        ],
                        "RowBr": 3,
                        "RowTl": 2,
                        "Text": "763,789,872.82",
                        "Type": "body"
                    },
                    {
                        "ColBr": 4,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 574,
                                "Y": 106
                            },
                            {
                                "X": 873,
                                "Y": 106
                            },
                            {
                                "X": 873,
                                "Y": 135
                            },
                            {
                                "X": 574,
                                "Y": 135
                            }
                        ],
                        "RowBr": 3,
                        "RowTl": 2,
                        "Text": "896,653,780.86",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 4,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 873,
                                "Y": 106
                            },
                            {
                                "X": 1166,
                                "Y": 105
                            },
                            {
                                "X": 1166,
                                "Y": 135
                            },
                            {
                                "X": 873,
                                "Y": 135
                            }
                        ],
                        "RowBr": 3,
                        "RowTl": 2,
                        "Text": "-11.42%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 135
                            },
                            {
                                "X": 348,
                                "Y": 135
                            },
                            {
                                "X": 348,
                                "Y": 198
                            },
                            {
                                "X": 32,
                                "Y": 198
                            }
                        ],
                        "RowBr": 4,
                        "RowTl": 3,
                        "Text": "",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 135
                            },
                            {
                                "X": 554,
                                "Y": 135
                            },
                            {
                                "X": 554,
                                "Y": 198
                            },
                            {
                                "X": 348,
                                "Y": 198
                            }
                        ],
                        "RowBr": 4,
                        "RowTl": 3,
                        "Text": "本报告期",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 135
                            },
                            {
                                "X": 789,
                                "Y": 135
                            },
                            {
                                "X": 789,
                                "Y": 198
                            },
                            {
                                "X": 554,
                                "Y": 198
                            }
                        ],
                        "RowBr": 4,
                        "RowTl": 3,
                        "Text": "本报告期比上年同期增减",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 135
                            },
                            {
                                "X": 997,
                                "Y": 135
                            },
                            {
                                "X": 997,
                                "Y": 198
                            },
                            {
                                "X": 789,
                                "Y": 198
                            }
                        ],
                        "RowBr": 4,
                        "RowTl": 3,
                        "Text": "年初至报告期末",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 135
                            },
                            {
                                "X": 1166,
                                "Y": 135
                            },
                            {
                                "X": 1166,
                                "Y": 198
                            },
                            {
                                "X": 997,
                                "Y": 198
                            }
                        ],
                        "RowBr": 4,
                        "RowTl": 3,
                        "Text": "年初至报告期末\n比上年同期增减",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 198
                            },
                            {
                                "X": 348,
                                "Y": 198
                            },
                            {
                                "X": 348,
                                "Y": 232
                            },
                            {
                                "X": 32,
                                "Y": 232
                            }
                        ],
                        "RowBr": 5,
                        "RowTl": 4,
                        "Text": "营业收入(元)",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 198
                            },
                            {
                                "X": 554,
                                "Y": 198
                            },
                            {
                                "X": 554,
                                "Y": 232
                            },
                            {
                                "X": 348,
                                "Y": 232
                            }
                        ],
                        "RowBr": 5,
                        "RowTl": 4,
                        "Text": "3,832,876,471.32",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 198
                            },
                            {
                                "X": 789,
                                "Y": 198
                            },
                            {
                                "X": 789,
                                "Y": 232
                            },
                            {
                                "X": 554,
                                "Y": 232
                            }
                        ],
                        "RowBr": 5,
                        "RowTl": 4,
                        "Text": "-19.41%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 198
                            },
                            {
                                "X": 997,
                                "Y": 198
                            },
                            {
                                "X": 997,
                                "Y": 232
                            },
                            {
                                "X": 789,
                                "Y": 232
                            }
                        ],
                        "RowBr": 5,
                        "RowTl": 4,
                        "Text": "89,678,082,87",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 198
                            },
                            {
                                "X": 1166,
                                "Y": 198
                            },
                            {
                                "X": 1166,
                                "Y": 232
                            },
                            {
                                "X": 997,
                                "Y": 232
                            }
                        ],
                        "RowBr": 5,
                        "RowTl": 4,
                        "Text": "-23,87%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 232
                            },
                            {
                                "X": 348,
                                "Y": 232
                            },
                            {
                                "X": 348,
                                "Y": 261
                            },
                            {
                                "X": 32,
                                "Y": 261
                            }
                        ],
                        "RowBr": 6,
                        "RowTl": 5,
                        "Text": "归属于上市公司股东的净利润(元)",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 232
                            },
                            {
                                "X": 554,
                                "Y": 232
                            },
                            {
                                "X": 554,
                                "Y": 261
                            },
                            {
                                "X": 348,
                                "Y": 261
                            }
                        ],
                        "RowBr": 6,
                        "RowTl": 5,
                        "Text": "-28,789,872.82",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 232
                            },
                            {
                                "X": 789,
                                "Y": 232
                            },
                            {
                                "X": 789,
                                "Y": 261
                            },
                            {
                                "X": 554,
                                "Y": 261
                            }
                        ],
                        "RowBr": 6,
                        "RowTl": 5,
                        "Text": "26.76%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 232
                            },
                            {
                                "X": 997,
                                "Y": 232
                            },
                            {
                                "X": 997,
                                "Y": 261
                            },
                            {
                                "X": 789,
                                "Y": 261
                            }
                        ],
                        "RowBr": 6,
                        "RowTl": 5,
                        "Text": "-78,982,652.98",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 232
                            },
                            {
                                "X": 1166,
                                "Y": 232
                            },
                            {
                                "X": 1166,
                                "Y": 261
                            },
                            {
                                "X": 997,
                                "Y": 261
                            }
                        ],
                        "RowBr": 6,
                        "RowTl": 5,
                        "Text": "46.87%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 261
                            },
                            {
                                "X": 348,
                                "Y": 261
                            },
                            {
                                "X": 348,
                                "Y": 321
                            },
                            {
                                "X": 32,
                                "Y": 322
                            }
                        ],
                        "RowBr": 7,
                        "RowTl": 6,
                        "Text": "归属于上市公司股东的扣除非经\n常性损益的净利润(元)",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 261
                            },
                            {
                                "X": 554,
                                "Y": 261
                            },
                            {
                                "X": 554,
                                "Y": 322
                            },
                            {
                                "X": 348,
                                "Y": 321
                            }
                        ],
                        "RowBr": 7,
                        "RowTl": 6,
                        "Text": "-32,282,770.51",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 261
                            },
                            {
                                "X": 789,
                                "Y": 261
                            },
                            {
                                "X": 789,
                                "Y": 322
                            },
                            {
                                "X": 554,
                                "Y": 322
                            }
                        ],
                        "RowBr": 7,
                        "RowTl": 6,
                        "Text": "46.62%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 261
                            },
                            {
                                "X": 997,
                                "Y": 261
                            },
                            {
                                "X": 997,
                                "Y": 322
                            },
                            {
                                "X": 789,
                                "Y": 322
                            }
                        ],
                        "RowBr": 7,
                        "RowTl": 6,
                        "Text": "-78,872,762.12",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 261
                            },
                            {
                                "X": 1166,
                                "Y": 261
                            },
                            {
                                "X": 1166,
                                "Y": 322
                            },
                            {
                                "X": 997,
                                "Y": 322
                            }
                        ],
                        "RowBr": 7,
                        "RowTl": 6,
                        "Text": "46.42%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 322
                            },
                            {
                                "X": 348,
                                "Y": 321
                            },
                            {
                                "X": 348,
                                "Y": 383
                            },
                            {
                                "X": 32,
                                "Y": 383
                            }
                        ],
                        "RowBr": 8,
                        "RowTl": 7,
                        "Text": "经营活动产生的现金流量净额(元)",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 321
                            },
                            {
                                "X": 554,
                                "Y": 322
                            },
                            {
                                "X": 554,
                                "Y": 383
                            },
                            {
                                "X": 348,
                                "Y": 383
                            }
                        ],
                        "RowBr": 8,
                        "RowTl": 7,
                        "Text": "18,647,940.25",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 322
                            },
                            {
                                "X": 789,
                                "Y": 322
                            },
                            {
                                "X": 789,
                                "Y": 383
                            },
                            {
                                "X": 554,
                                "Y": 383
                            }
                        ],
                        "RowBr": 8,
                        "RowTl": 7,
                        "Text": "42.16%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 322
                            },
                            {
                                "X": 997,
                                "Y": 322
                            },
                            {
                                "X": 997,
                                "Y": 383
                            },
                            {
                                "X": 789,
                                "Y": 383
                            }
                        ],
                        "RowBr": 8,
                        "RowTl": 7,
                        "Text": "-41,784,760,76",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 322
                            },
                            {
                                "X": 1166,
                                "Y": 322
                            },
                            {
                                "X": 1166,
                                "Y": 383
                            },
                            {
                                "X": 997,
                                "Y": 383
                            }
                        ],
                        "RowBr": 8,
                        "RowTl": 7,
                        "Text": "-77.76%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 383
                            },
                            {
                                "X": 348,
                                "Y": 383
                            },
                            {
                                "X": 348,
                                "Y": 416
                            },
                            {
                                "X": 32,
                                "Y": 416
                            }
                        ],
                        "RowBr": 9,
                        "RowTl": 8,
                        "Text": "基本每股收益(元/股)",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 383
                            },
                            {
                                "X": 554,
                                "Y": 383
                            },
                            {
                                "X": 554,
                                "Y": 416
                            },
                            {
                                "X": 348,
                                "Y": 416
                            }
                        ],
                        "RowBr": 9,
                        "RowTl": 8,
                        "Text": "-0.0541",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 383
                            },
                            {
                                "X": 789,
                                "Y": 383
                            },
                            {
                                "X": 789,
                                "Y": 416
                            },
                            {
                                "X": 554,
                                "Y": 416
                            }
                        ],
                        "RowBr": 9,
                        "RowTl": 8,
                        "Text": "38.12%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 383
                            },
                            {
                                "X": 997,
                                "Y": 383
                            },
                            {
                                "X": 997,
                                "Y": 416
                            },
                            {
                                "X": 789,
                                "Y": 416
                            }
                        ],
                        "RowBr": 9,
                        "RowTl": 8,
                        "Text": "-0.872",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 383
                            },
                            {
                                "X": 1166,
                                "Y": 383
                            },
                            {
                                "X": 1166,
                                "Y": 416
                            },
                            {
                                "X": 997,
                                "Y": 416
                            }
                        ],
                        "RowBr": 9,
                        "RowTl": 8,
                        "Text": "47.87%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 416
                            },
                            {
                                "X": 348,
                                "Y": 416
                            },
                            {
                                "X": 348,
                                "Y": 444
                            },
                            {
                                "X": 32,
                                "Y": 444
                            }
                        ],
                        "RowBr": 10,
                        "RowTl": 9,
                        "Text": "稀释每股收益(元/股)",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 416
                            },
                            {
                                "X": 554,
                                "Y": 416
                            },
                            {
                                "X": 554,
                                "Y": 444
                            },
                            {
                                "X": 348,
                                "Y": 444
                            }
                        ],
                        "RowBr": 10,
                        "RowTl": 9,
                        "Text": "-0.0541",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 416
                            },
                            {
                                "X": 789,
                                "Y": 416
                            },
                            {
                                "X": 789,
                                "Y": 444
                            },
                            {
                                "X": 554,
                                "Y": 444
                            }
                        ],
                        "RowBr": 10,
                        "RowTl": 9,
                        "Text": "38.12%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 416
                            },
                            {
                                "X": 997,
                                "Y": 416
                            },
                            {
                                "X": 997,
                                "Y": 444
                            },
                            {
                                "X": 789,
                                "Y": 444
                            }
                        ],
                        "RowBr": 10,
                        "RowTl": 9,
                        "Text": "-0.872",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 416
                            },
                            {
                                "X": 1166,
                                "Y": 416
                            },
                            {
                                "X": 1166,
                                "Y": 444
                            },
                            {
                                "X": 997,
                                "Y": 444
                            }
                        ],
                        "RowBr": 10,
                        "RowTl": 9,
                        "Text": "47.87%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 1,
                        "ColTl": 0,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 32,
                                "Y": 444
                            },
                            {
                                "X": 348,
                                "Y": 444
                            },
                            {
                                "X": 348,
                                "Y": 475
                            },
                            {
                                "X": 32,
                                "Y": 475
                            }
                        ],
                        "RowBr": 11,
                        "RowTl": 10,
                        "Text": "加权平均净资产收益率",
                        "Type": "body"
                    },
                    {
                        "ColBr": 2,
                        "ColTl": 1,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 348,
                                "Y": 444
                            },
                            {
                                "X": 554,
                                "Y": 444
                            },
                            {
                                "X": 554,
                                "Y": 475
                            },
                            {
                                "X": 348,
                                "Y": 475
                            }
                        ],
                        "RowBr": 11,
                        "RowTl": 10,
                        "Text": "-6.21%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 3,
                        "ColTl": 2,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 554,
                                "Y": 444
                            },
                            {
                                "X": 789,
                                "Y": 444
                            },
                            {
                                "X": 789,
                                "Y": 475
                            },
                            {
                                "X": 554,
                                "Y": 475
                            }
                        ],
                        "RowBr": 11,
                        "RowTl": 10,
                        "Text": "-8.65%",
                        "Type": "body"
                    },
                    {
                        "ColBr": 5,
                        "ColTl": 3,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 789,
                                "Y": 444
                            },
                            {
                                "X": 997,
                                "Y": 444
                            },
                            {
                                "X": 998,
                                "Y": 475
                            },
                            {
                                "X": 789,
                                "Y": 475
                            }
                        ],
                        "RowBr": 11,
                        "RowTl": 10,
                        "Text": "-13.78",
                        "Type": "body"
                    },
                    {
                        "ColBr": 6,
                        "ColTl": 5,
                        "Confidence": 100,
                        "Polygon": [
                            {
                                "X": 997,
                                "Y": 444
                            },
                            {
                                "X": 1166,
                                "Y": 444
                            },
                            {
                                "X": 1166,
                                "Y": 475
                            },
                            {
                                "X": 998,
                                "Y": 475
                            }
                        ],
                        "RowBr": 11,
                        "RowTl": 10,
                        "Text": "-8.65%",
                        "Type": "body"
                    }
                ],
                "TableCoordPoint": [
                    {
                        "X": 32,
                        "Y": 29
                    },
                    {
                        "X": 1166,
                        "Y": 29
                    },
                    {
                        "X": 1166,
                        "Y": 475
                    },
                    {
                        "X": 32,
                        "Y": 475
                    }
                ],
                "Type": 1
            }
        ]
    }
}
```

