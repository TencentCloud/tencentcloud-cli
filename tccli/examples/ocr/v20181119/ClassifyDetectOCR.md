**Example 1: 智能卡证分类示例代码**



Input: 

```
tccli ocr ClassifyDetectOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --DiscernType BankCard
```

Output: 
```
{
    "Response": {
        "ClassifyDetectInfos": [
            {
                "Name": "银行卡",
                "Type": "BankCard",
                "Rect": {
                    "X": 0,
                    "Y": 0,
                    "Width": 750,
                    "Height": 520
                }
            }
        ],
        "RequestId": "46ab2e62-11e3-4d04-9fab-0abe18e7c927"
    }
}
```

