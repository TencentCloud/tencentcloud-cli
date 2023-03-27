**Example 1: 财报识别示例代码**

财报识别

Input: 

```
tccli ocr RecognizeFinancialReportOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "770d1ec1-9bbf-4ec3-876c-5b6b66fc5c8c",
        "Tables": [
            {
                "Type": "3",
                "Head": [
                    {
                        "Col": 1,
                        "Text": "项目",
                        "Rect": "313,366,760,39"
                    },
                    {
                        "Col": 2,
                        "Text": "本期发生额",
                        "Rect": "1073,366,310,40"
                    },
                    {
                        "Col": 3,
                        "Text": "上期发生额",
                        "Rect": "1383,366,310,40"
                    }
                ],
                "Rows": [
                    {
                        "Row": 2,
                        "Cells": [
                            {
                                "Col": 1,
                                "Text": "、经营活动产生的现金流量:",
                                "Rect": "313,366,760,39"
                            },
                            {
                                "Col": 2,
                                "Text": "",
                                "Rect": "1073,366,310,40"
                            },
                            {
                                "Col": 3,
                                "Text": "",
                                "Rect": "1383,366,310,40"
                            }
                        ]
                    },
                    {
                        "Row": 3,
                        "Cells": [
                            {
                                "Col": 1,
                                "Text": "销售商品提供劳务收到的现金",
                                "Rect": "313,404,760,42"
                            },
                            {
                                "Col": 2,
                                "Text": "1.609.403.170.56",
                                "Rect": "1073,405,310,41"
                            },
                            {
                                "Col": 3,
                                "Text": "843.734.421.08",
                                "Rect": "1383,406,310,40"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

