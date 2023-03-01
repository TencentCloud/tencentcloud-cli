**Example 1: 混贴票据识别示例代码（识别全部类型）**

混贴票据识别示例代码（识别全部类型）

Input: 

```
tccli ocr MixedInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "MixedInvoiceItems": [
            {
                "Type": 13,
                "Rect": {
                    "X": 20,
                    "Y": 891,
                    "Width": 479,
                    "Height": 597
                },
                "Angle": 0,
                "SingleInvoiceInfos": [
                    {
                        "Name": "发票号码",
                        "Value": "27357827",
                        "Row": 0
                    },
                    {
                        "Name": "日期",
                        "Value": "2016年04月11日",
                        "Row": 0
                    },
                    {
                        "Name": "发票代码",
                        "Value": "440300708461",
                        "Row": 0
                    },
                    {
                        "Name": "金额",
                        "Value": "778",
                        "Row": 0
                    }
                ],
                "Code": "OK"
            },
            {
                "Type": 2,
                "Rect": {
                    "X": 520,
                    "Y": 904,
                    "Width": 455,
                    "Height": 286
                },
                "Angle": 0,
                "SingleInvoiceInfos": [
                    {
                        "Name": "编号",
                        "Value": "Z96X809511",
                        "Row": 0
                    },
                    {
                        "Name": "出发站",
                        "Value": "上海",
                        "Row": 0
                    },
                    {
                        "Name": "到达站",
                        "Value": "南京",
                        "Row": 0
                    },
                    {
                        "Name": "出发时间",
                        "Value": "2018年03月06日18:51",
                        "Row": 0
                    },
                    {
                        "Name": "车次",
                        "Value": "Z196",
                        "Row": 0
                    },
                    {
                        "Name": "座位号",
                        "Value": "",
                        "Row": 0
                    },
                    {
                        "Name": "姓名",
                        "Value": "周周",
                        "Row": 0
                    },
                    {
                        "Name": "票价",
                        "Value": "46.5",
                        "Row": 0
                    },
                    {
                        "Name": "席别",
                        "Value": "新空调硬座",
                        "Row": 0
                    }
                ],
                "Code": "OK"
            }
        ],
        "RequestId": "d5202318-7dfa-4b34-9f1f-f21f36f43d67"
    }
}
```

**Example 2: 混贴票据识别示例代码（识别指定类型）**

混贴票据识别示例代码（识别指定类型）

Input: 

```
tccli ocr MixedInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --Types 2
```

Output: 
```
{
    "Response": {
        "MixedInvoiceItems": [
            {
                "Rect": {
                    "X": 31,
                    "Y": 34,
                    "Width": 1327,
                    "Height": 866
                },
                "Angle": 0,
                "SingleInvoiceInfos": [],
                "Code": "OK",
                "Type": 3
            },
            {
                "Rect": {
                    "X": 18,
                    "Y": 887,
                    "Width": 484,
                    "Height": 607
                },
                "Angle": 0,
                "SingleInvoiceInfos": [],
                "Code": "OK",
                "Type": 13
            },
            {
                "Rect": {
                    "X": 517,
                    "Y": 931,
                    "Width": 464,
                    "Height": 306
                },
                "Angle": 0,
                "SingleInvoiceInfos": [
                    {
                        "Name": "编号",
                        "Value": "Z96X089511",
                        "Row": 0
                    },
                    {
                        "Name": "出发站",
                        "Value": "上海",
                        "Row": 0
                    },
                    {
                        "Name": "车次",
                        "Value": "Z196",
                        "Row": 0
                    },
                    {
                        "Name": "到达站",
                        "Value": "南京",
                        "Row": 0
                    },
                    {
                        "Name": "出发时间",
                        "Value": "2018年03月06日18:51",
                        "Row": 0
                    },
                    {
                        "Name": "座位号",
                        "Value": "02车016号",
                        "Row": 0
                    },
                    {
                        "Name": "票价",
                        "Value": "46.50",
                        "Row": 0
                    },
                    {
                        "Name": "席别",
                        "Value": "新空调硬座",
                        "Row": 0
                    },
                    {
                        "Name": "身份证号",
                        "Value": "3210231991****6666",
                        "Row": 0
                    },
                    {
                        "Name": "姓名",
                        "Value": "周周",
                        "Row": 0
                    }
                ],
                "Code": "OK",
                "Type": 2
            }
        ],
        "RequestId": "6b261226-7255-4f56-ab51-a641106618ff"
    }
}
```

