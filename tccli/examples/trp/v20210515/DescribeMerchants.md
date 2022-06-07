**Example 1: 查询商户列表**



Input: 

```
tccli trp DescribeMerchants --cli-unfold-argument  \
    --Name  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Merchants": [
            {
                "Remark": "xx",
                "Name": "xx",
                "CorpId": 0,
                "UpdateTime": "xx",
                "MerchantId": "xx",
                "CodeRule": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

