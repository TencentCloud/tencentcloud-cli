**Example 1: 我的域名列表**



Input: 

```
tccli domain DescribeDomainNameList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "DomainSet": [
            {
                "AutoRenew": 0,
                "IsPremium": false,
                "DomainId": "domain-ji1p1g4q",
                "ExpirationDate": "2022-09-11",
                "DomainName": "tencent.com",
                "CodeTld": "com",
                "CreationDate": "2019-09-11",
                "Tld": ".com",
                "BuyStatus": "AboutToExpire"
            }
        ],
        "RequestId": "6cbc0aca-a3ba-42aa-8ced-ae7b93f56049"
    }
}
```

