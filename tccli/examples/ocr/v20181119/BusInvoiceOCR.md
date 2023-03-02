**Example 1: 汽车票识别示例代码**

汽车票识别

Input: 

```
tccli ocr BusInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "BusInvoiceInfos": [
            {
                "Name": "发票代码",
                "Value": "440600014",
                "Rect": {
                    "X": 601,
                    "Y": 204,
                    "Width": 64,
                    "Height": 17
                }
            },
            {
                "Name": "发票号码",
                "Value": "1010091024",
                "Rect": {
                    "X": 588,
                    "Y": 229,
                    "Width": 59,
                    "Height": 15
                }
            },
            {
                "Name": "日期",
                "Value": "2010年02月08日",
                "Rect": {
                    "X": 569,
                    "Y": 291,
                    "Width": 81,
                    "Height": 17
                }
            },
            {
                "Name": "始发地",
                "Value": "宝安",
                "Rect": {
                    "X": 344,
                    "Y": 255,
                    "Width": 58,
                    "Height": 21
                }
            },
            {
                "Name": "目的地",
                "Value": "武汉",
                "Rect": {
                    "X": 566,
                    "Y": 246,
                    "Width": 39,
                    "Height": 22
                }
            },
            {
                "Name": "票价",
                "Value": "490.00",
                "Rect": {
                    "X": 343,
                    "Y": 342,
                    "Width": 47,
                    "Height": 22
                }
            }
        ],
        "Angle": 358,
        "RequestId": "64b4f1c4-05bd-489a-88fc-30238ff546bd"
    }
}
```

