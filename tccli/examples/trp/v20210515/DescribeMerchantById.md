**Example 1: 查询商户信息**



Input: 

```
tccli trp DescribeMerchantById --cli-unfold-argument  \
    --MerchantId eqdmnz7020bmtvi9
```

Output: 
```
{
    "Response": {
        "Merchant": {
            "MerchantId": "eqdmnz7020bmtvi9",
            "CorpId": 10000,
            "Name": "demo",
            "Remark": "abcdd",
            "CreateTime": "2021-11-30T08:19:40.000Z",
            "UpdateTime": "2021-12-06T08:09:17.000Z",
            "CodeRule": "^https://anxin.mtest.qq.com/qr/eqdmnz7020bmtvi9_(.*)"
        },
        "RequestId": "55fa060c-fa0a-4704-a8b5-08ce336192a4"
    }
}
```

