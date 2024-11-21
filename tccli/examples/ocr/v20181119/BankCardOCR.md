**Example 1: BankCardOCR调用**



Input: 

```
tccli ocr BankCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/BankCardOCR/BankCardOCR1.jpg
```

Output: 
```
{
    "Response": {
        "BankInfo": "招商银行(03080000)",
        "BorderCutImage": null,
        "CardName": "招商银行信用卡",
        "CardNo": "6225768888888888",
        "CardNoImage": null,
        "CardType": "贷记卡",
        "QualityValue": null,
        "RequestId": "4a4438c5-09ff-4031-945c-17000ba4542d",
        "ValidDate": "07/2023",
        "WarningCode": null
    }
}
```

