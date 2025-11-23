**Example 1: 查询批量创建私有域结果**



Input: 

```
tccli privatedns DescribeCreateZoneListResult --cli-unfold-argument  \
    --Domains 1.com 2.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845",
        "ZonesInfo": [
            {
                "Domain": "1.com",
                "ZoneId": "zone-id1",
                "Reason": null
            },
            {
                "Domain": "2.com",
                "ZoneId": null,
                "Reason": "创建失败"
            }
        ]
    }
}
```

