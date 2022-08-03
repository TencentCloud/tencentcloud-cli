**Example 1: 查询保护网站**



Input: 

```
tccli bma DescribeBPProtectURLs --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "ProtectURLInfos": [
            {
                "ProtectURLId": 123,
                "ProtectURL": "xxx",
                "ProtectWeb": "xxx",
                "ProtectURLStatus": 1,
                "ProtectURLNote": "xxx",
                "CreateTime": "xxx"
            }
        ],
        "TotalCount": 10,
        "RequestId": "xxx"
    }
}
```

