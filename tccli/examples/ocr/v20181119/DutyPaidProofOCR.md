**Example 1: 完税证明识别示例代码**

完税证明识别

Input: 

```
tccli ocr DutyPaidProofOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "DutyPaidProofInfos": [
            {
                "Name": "税务机关",
                "Value": "武昌市国家税务局第-税务分局",
                "Rect": {
                    "X": 658,
                    "Y": 152,
                    "Width": 283,
                    "Height": 20
                }
            },
            {
                "Name": "税号",
                "Value": "2820000",
                "Rect": {
                    "X": 759,
                    "Y": 128,
                    "Width": 209,
                    "Height": 21
                }
            },
            {
                "Name": "纳税人识别号",
                "Value": "440524100000",
                "Rect": {
                    "X": 161,
                    "Y": 182,
                    "Width": 131,
                    "Height": 19
                }
            },
            {
                "Name": "纳税人名称",
                "Value": "李明",
                "Rect": {
                    "X": 629,
                    "Y": 182,
                    "Width": 31,
                    "Height": 19
                }
            },
            {
                "Name": "金额合计大写",
                "Value": "壹仟肆佰柒拾陆元叁角玖分",
                "Rect": {
                    "X": 214,
                    "Y": 505,
                    "Width": 167,
                    "Height": 20
                }
            },
            {
                "Name": "金额合计小写",
                "Value": "¥1476.39",
                "Rect": {
                    "X": 830,
                    "Y": 505,
                    "Width": 70,
                    "Height": 19
                }
            },
            {
                "Name": "填票人",
                "Value": "李菲",
                "Rect": {
                    "X": 346,
                    "Y": 611,
                    "Width": 46,
                    "Height": 19
                }
            }
        ],
        "Angle": 0,
        "RequestId": "da6ecc00-a7df-4896-95e9-1d0930e40fde"
    }
}
```

