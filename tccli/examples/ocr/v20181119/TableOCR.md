**Example 1: 表格识别示例代码**

表格识别示例代码

Input: 

```
tccli ocr TableOCR --cli-unfold-argument  \
    --ImageUrl http%3A%2F%2Fimg3.redocn.com%2Ftupian%2F20180301%2Fkongbaiqiuzhijianlibiaogesheji_9230633.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "ColTl": -1,
                "RowTl": -1,
                "ColBr": -1,
                "RowBr": -1,
                "Text": "项号商品",
                "Type": "header",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 3378,
                        "Y": 363
                    },
                    {
                        "X": 3383,
                        "Y": 646
                    },
                    {
                        "X": 3304,
                        "Y": 648
                    },
                    {
                        "X": 3299,
                        "Y": 365
                    }
                ],
                "AdvancedInfo": "{}"
            },
            {
                "ColTl": -1,
                "RowTl": -1,
                "ColBr": -1,
                "RowBr": -1,
                "Text": "菜/:11181 1 19医101",
                "Type": "header",
                "Confidence": 53,
                "Polygon": [
                    {
                        "X": 3470,
                        "Y": 1285
                    },
                    {
                        "X": 3501,
                        "Y": 3092
                    },
                    {
                        "X": 3361,
                        "Y": 3094
                    },
                    {
                        "X": 3330,
                        "Y": 1287
                    }
                ],
                "AdvancedInfo": "{}"
            },
            {
                "ColTl": -1,
                "RowTl": -1,
                "ColBr": -1,
                "RowBr": -1,
                "Text": "中华人民共和国海关出☐货物报关单",
                "Type": "header",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 3201,
                        "Y": 2046
                    },
                    {
                        "X": 3211,
                        "Y": 2618
                    },
                    {
                        "X": 3169,
                        "Y": 2618
                    },
                    {
                        "X": 3159,
                        "Y": 2046
                    }
                ],
                "AdvancedInfo": "{}"
            },
            {
                "ColTl": -1,
                "RowTl": -1,
                "ColBr": -1,
                "RowBr": -1,
                "Text": "生产销售单位公司名(必填)",
                "Type": "header",
                "Confidence": 98,
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
                "AdvancedInfo": "{}"
            }
        ],
        "Data": "bWxQSwECFAAUAAAACAAAAAAAcxSJldcBAAD9BQAADQAAAAAAAAAAAAAAAACtLAAAeGwvc3R5bGVzLnhtbFBLAQIUABQAAAAIAAAAAAC8TIYcSAYAAP4kAAATAAAAAAAAAAAAAAAAAK8uAAB4bC90aGVtZS90aGVtZTEueG1sUEsBAhQAFAAAAAgAAAAAANG5P9oECwAAUU0AABgAAAAAAAAAAAAAAAAAKDUAAHhsL3dvcmtzaGVldHMvc2hlZXQyLnhtbFBLAQIUABQAAAAIAAAAAADjsY7PqAMAAE8PAAAYAAAAAAAAAAAAAAAAAGJAAAB4bC93b3Jrc2hlZXRzL3NoZWV0MS54bWxQSwUGAAAAAAwADAALAwAAQEQAAAAA",
        "RequestId": "98f8fcbf-933a-4e95-ac48-6f1a9308fs53"
    }
}
```

