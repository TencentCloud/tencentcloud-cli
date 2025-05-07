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
        "CardCategory": "标准实体银行卡",
        "CardName": "招商银行信用卡",
        "CardNo": "6225768888888888",
        "CardNoImage": null,
        "CardType": "贷记卡",
        "QualityValue": null,
        "RequestId": "4eeb7002-ef18-46b1-92dc-21e836f27d7f",
        "ValidDate": "07/2023",
        "WarningCode": null
    }
}
```

