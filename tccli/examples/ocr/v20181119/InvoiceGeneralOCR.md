**Example 1: 通用机打发票识别示例代码**

通用机打发票识别

Input: 

```
tccli ocr InvoiceGeneralOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "InvoiceGeneralInfos": [
            {
                "Name": "校验码",
                "Value": "15634318038000000",
                "Rect": {
                    "X": 278,
                    "Y": 297,
                    "Width": 194,
                    "Height": 19
                }
            },
            {
                "Name": "发票代码",
                "Value": "1440310000",
                "Rect": {
                    "X": 879,
                    "Y": 72,
                    "Width": 195,
                    "Height": 23
                }
            },
            {
                "Name": "发票号码",
                "Value": "01648000",
                "Rect": {
                    "X": 874,
                    "Y": 109,
                    "Width": 129,
                    "Height": 22
                }
            },
            {
                "Name": "日期",
                "Value": "2018年1月22日",
                "Rect": {
                    "X": 205,
                    "Y": 151,
                    "Width": 121,
                    "Height": 18
                }
            },
            {
                "Name": "购买方识别号",
                "Value": "91440300000XG",
                "Rect": {
                    "X": 180,
                    "Y": 618,
                    "Width": 197,
                    "Height": 20
                }
            },
            {
                "Name": "销售方识别号",
                "Value": "4403006700004",
                "Rect": {
                    "X": 274,
                    "Y": 250,
                    "Width": 147,
                    "Height": 20
                }
            },
            {
                "Name": "合计金额(大写)",
                "Value": "玖仟元整",
                "Rect": {
                    "X": 301,
                    "Y": 579,
                    "Width": 83,
                    "Height": 22
                }
            },
            {
                "Name": "购买方名称",
                "Value": "腾讯科技(深圳)有限公司",
                "Rect": {
                    "X": 274,
                    "Y": 198,
                    "Width": 225,
                    "Height": 24
                }
            },
            {
                "Name": "合计金额(小写)",
                "Value": "9000.00",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 1,
                    "Height": 1
                }
            }
        ],
        "Angle": 0,
        "RequestId": "fd7e1fe1-1039-4d28-9376-6e144dbd3741"
    }
}
```

