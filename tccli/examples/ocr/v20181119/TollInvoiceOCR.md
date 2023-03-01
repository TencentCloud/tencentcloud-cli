**Example 1: 过路过桥费发票识别示例代码**

过路过桥费发票识别

Input: 

```
tccli ocr TollInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "TollInvoiceInfos": [
            {
                "Name": "发票代码",
                "Value": "144700221",
                "Rect": {
                    "X": 231,
                    "Y": 178,
                    "Width": 181,
                    "Height": 21
                }
            },
            {
                "Name": "发票号码",
                "Value": "2737827",
                "Rect": {
                    "X": 232,
                    "Y": 212,
                    "Width": 130,
                    "Height": 26
                }
            },
            {
                "Name": "日期",
                "Value": "18/08/07",
                "Rect": {
                    "X": 277,
                    "Y": 426,
                    "Width": 174,
                    "Height": 20
                }
            },
            {
                "Name": "金额",
                "Value": "5",
                "Rect": {
                    "X": 192,
                    "Y": 426,
                    "Width": 13,
                    "Height": 19
                }
            },
            {
                "Name": "入口",
                "Value": "前海",
                "Rect": {
                    "X": 194,
                    "Y": 286,
                    "Width": 33,
                    "Height": 21
                }
            },
            {
                "Name": "出口",
                "Value": "大铲湾",
                "Rect": {
                    "X": 302,
                    "Y": 287,
                    "Width": 52,
                    "Height": 20
                }
            }
        ],
        "Angle": 0,
        "RequestId": "e1d01d6e-a2cd-475b-8dd4-3655b61c8b7a"
    }
}
```

