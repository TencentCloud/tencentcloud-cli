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
            "CodeRule": "https://xxx.xxx.com/qr/eqdmnz7020bmtvi9_(.*)",
            "CodeType": 0,
            "CodeUrl": "https://xxx.xxx.com"
        },
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

