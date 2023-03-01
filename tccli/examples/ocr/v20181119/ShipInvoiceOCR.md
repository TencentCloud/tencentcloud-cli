**Example 1: 轮船票识别示例代码**

轮船票识别

Input: 

```
tccli ocr ShipInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "ShipInvoiceInfos": [
            {
                "Name": "发票代码",
                "Value": "144041570120",
                "Rect": {
                    "X": 217,
                    "Y": 233,
                    "Width": 170,
                    "Height": 21
                }
            },
            {
                "Name": "发票号码",
                "Value": "00910368",
                "Rect": {
                    "X": 221,
                    "Y": 260,
                    "Width": 111,
                    "Height": 22
                }
            },
            {
                "Name": "日期",
                "Value": "2015年11月20日",
                "Rect": {
                    "X": 167,
                    "Y": 334,
                    "Width": 199,
                    "Height": 27
                }
            },
            {
                "Name": "始发地",
                "Value": "九洲港",
                "Rect": {
                    "X": 140,
                    "Y": 290,
                    "Width": 69,
                    "Height": 25
                }
            },
            {
                "Name": "目的地",
                "Value": "中港城码头",
                "Rect": {
                    "X": 289,
                    "Y": 289,
                    "Width": 116,
                    "Height": 28
                }
            },
            {
                "Name": "票价",
                "Value": "175.00",
                "Rect": {
                    "X": 152,
                    "Y": 372,
                    "Width": 61,
                    "Height": 19
                }
            }
        ],
        "Angle": 351,
        "RequestId": "64fd29cc-dcc4-459b-a5bd-71fb8abfd500"
    }
}
```

