**Example 1: 查询指定防护实例的详情**

按防护实例 ID 过滤，查询 `prot-0004c045b8` 的详细信息。

Input: 

```
tccli antiddos DescribeProtections --cli-unfold-argument  \
    --Filters.0.Name ProtectionId \
    --Filters.0.Values prot-0004c045b8
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Protections": [
            {
                "ProtectionId": "prot-0004c045b8",
                "Name": "protection_name",
                "ProtectionLevel": "advanced",
                "Status": "protecting",
                "Tags": [
                    {
                        "TagKey": "business",
                        "TagValue": "protection"
                    }
                ]
            }
        ],
        "RequestId": "641a08e3-2ef7-407c-9c2f-2a9928741df5"
    }
}
```

