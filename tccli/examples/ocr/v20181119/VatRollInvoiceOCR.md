**Example 1: 增值税发票（卷票）识别示例代码**

增值税发票（卷票）识别

Input: 

```
tccli ocr VatRollInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "VatRollInvoiceInfos": [
            {
                "Name": "发票代码",
                "Value": "033000101",
                "Rect": {
                    "X": 67,
                    "Y": 246,
                    "Width": 324,
                    "Height": 25
                }
            },
            {
                "Name": "发票号码",
                "Value": "14547954",
                "Rect": {
                    "X": 67,
                    "Y": 281,
                    "Width": 253,
                    "Height": 27
                }
            },
            {
                "Name": "销售方识别号",
                "Value": "9133974410525",
                "Rect": {
                    "X": 216,
                    "Y": 404,
                    "Width": 202,
                    "Height": 21
                }
            },
            {
                "Name": "开票日期",
                "Value": "2019-07-14",
                "Rect": {
                    "X": 168,
                    "Y": 428,
                    "Width": 193,
                    "Height": 22
                }
            },
            {
                "Name": "购买方识别号",
                "Value": "913302572467",
                "Rect": {
                    "X": 215,
                    "Y": 513,
                    "Width": 203,
                    "Height": 21
                }
            },
            {
                "Name": "合计金额(小写)",
                "Value": "¥200.00",
                "Rect": {
                    "X": 203,
                    "Y": 1022,
                    "Width": 87,
                    "Height": 23
                }
            },
            {
                "Name": "合计金额(大写)",
                "Value": "贰佰圆整",
                "Rect": {
                    "X": 201,
                    "Y": 1051,
                    "Width": 87,
                    "Height": 23
                }
            },
            {
                "Name": "校验码",
                "Value": "839310540000",
                "Rect": {
                    "X": 183,
                    "Y": 1081,
                    "Width": 220,
                    "Height": 20
                }
            }
        ],
        "Angle": 0,
        "RequestId": "a0513eeb-6747-4a35-91ad-addcd1392896"
    }
}
```

