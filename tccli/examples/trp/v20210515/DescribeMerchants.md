**Example 1: 查询商户列表**



Input: 

```
tccli trp DescribeMerchants --cli-unfold-argument  \
    --Name 商户名称 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Merchants": [
            {
                "Remark": "商户备注信息",
                "Name": "商户名称",
                "CorpId": 10000,
                "UpdateTime": "2023-08-15T02:47:35.000Z",
                "MerchantId": "pn30msjjxwga",
                "CodeRule": "https://xxx.xxx.com/qr/(.*)",
                "CreateTime": "2023-08-15T02:47:35.000Z",
                "CodeType": 0,
                "CodeUrl": "https://xxx.xxx.com"
            }
        ],
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

