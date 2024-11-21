**Example 1: ClassifyDetectOCR调用**



Input: 

```
tccli ocr ClassifyDetectOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
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

