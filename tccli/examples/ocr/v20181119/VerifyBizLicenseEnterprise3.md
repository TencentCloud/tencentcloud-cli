**Example 1: 三要素**



Input: 

```
tccli ocr VerifyBizLicenseEnterprise3 --cli-unfold-argument  \
    --CreditCode 12xxxxxxxxx3 \
    --EntName xxxxx生鲜食品超市（个体工商户） \
    --LrName 刘xxxxx \
    --VerifyType ENT_3META
```

Output: 
```
{
    "Response": {
        "RequestId": "ff3cb900-6961-402f-bb25-45b86cb6f695",
        "StatusCode": 0,
        "VerifyResult": 1,
        "OperatingStatus": "1"
    }
}
```

