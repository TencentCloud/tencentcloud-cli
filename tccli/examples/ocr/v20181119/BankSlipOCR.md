**Example 1: 银行回单识别示例代码**

银行回单识别

Input: 

```
tccli ocr BankSlipOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "BankSlipInfos": [
            {
                "Rect": {
                    "Y": 629,
                    "X": 182,
                    "Height": 19,
                    "Width": 31
                },
                "Name": "日期",
                "Value": "2020年08月24日"
            }
        ],
        "Angle": 0,
        "RequestId": "da6ecc00-a7df-4896-95e9-1d0930e40fde"
    }
}
```

