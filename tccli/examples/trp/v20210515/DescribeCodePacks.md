**Example 1: 查询码包列表**



Input: 

```
tccli trp DescribeCodePacks --cli-unfold-argument  \
    --Keyword  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "CodePacks": [
            {
                "PackId": "m81h3z1fsi5yifmn05",
                "CorpId": 10000,
                "MerchantId": "eqdmnz7020bmtvi9",
                "CreateTime": "2021-12-01T11:24:17.000Z",
                "UpdateTime": "2021-12-01T11:24:17.000Z",
                "Status": "done",
                "Log": null,
                "CreateUser": "100000118465",
                "Amount": 121,
                "CodeLength": 18,
                "CodeType": "number",
                "Cipher": 0,
                "TextUrl": null,
                "PackUrl": null,
                "MerchantName": "demo"
            }
        ],
        "TotalCount": 11,
        "RequestId": "b7dfc004-bad6-47f9-b74e-5765ff42bc3f"
    }
}
```

