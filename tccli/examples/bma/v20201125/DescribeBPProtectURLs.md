**Example 1: 查询保护网站**



Input: 

```
tccli bma DescribeBPProtectURLs --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1 \
    --CompanyId 123
```

Output: 
```
{
    "Response": {
        "ProtectURLInfos": [
            {
                "CreateTime": "xxx",
                "ProtectURL": "xxx",
                "ProtectURLId": 123,
                "ProtectURLStatus": 1,
                "ProtectURLNote": "xxx"
            }
        ],
        "TotalCount": 10,
        "RequestId": "xxx"
    }
}
```

