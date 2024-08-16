**Example 1: 门头照识别示例**

门头照识别示例

Input: 

```
tccli ocr RecognizeStoreName --cli-unfold-argument  \
    --ImageBase64 
```

Output: 
```
{
    "Response": {
        "Angle": 0.988696813583374,
        "RequestId": "e450a988-e6b1-4dde-810c-59ab214d39a6",
        "StoreInfo": [
            {
                "Name": "商店名称",
                "Rect": {
                    "Height": 263,
                    "Width": 1132,
                    "X": 232,
                    "Y": 366
                },
                "Value": "城市生活超市"
            },
            {
                "Name": "商店名称",
                "Rect": {
                    "Height": 69,
                    "Width": 275,
                    "X": 240,
                    "Y": 557
                },
                "Value": "CITY LIFE"
            }
        ],
        "StoreLabel": [
            "门头照"
        ]
    }
}
```

