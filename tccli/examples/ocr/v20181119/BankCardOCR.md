**Example 1: 银行卡识别示例代码**



Input: 

```
tccli ocr BankCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "BankInfo": "招商银行(03080000)",
        "ValidDate": "07/2023",
        "CardType": "贷记卡",
        "CardName": "招商银行信用卡",
        "BorderCutImage": null,
        "CardNoImage": null,
        "QualityValue": 80,
        "WarningCode": [
            -9110
        ],
        "CardNo": "6225768888888888",
        "RequestId": "68f8fcbf-6004-0111a-ac18-6f1a9308fs100mab"
    }
}
```

