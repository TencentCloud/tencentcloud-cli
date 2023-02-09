**Example 1: acceleration_domains**

查询指定domain-id的加速域名信息。

Input: 

```
tccli teo DescribeAccelerationDomains --cli-unfold-argument  \
    --Direction desc \
    --ZoneId zone-20hyebgyfsko \
    --Limit 0 \
    --Filters.0.Fuzzy True \
    --Filters.0.Values domain-3d5dg39c \
    --Filters.0.Name domain-id \
    --Offset 0 \
    --Order created_on \
    --Match all
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "AccelerationDomains": [
            {
                "DomainName": "example.qq.com",
                "ModifiedOn": "2020-09-22T00:00:00+00:00",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "DomainStatus": "online",
                "ZoneId": "zone-20hyebgyfsko",
                "Cname": "example.qq.com.cname.com",
                "OriginDetail": {
                    "Origin": "qq.com",
                    "OriginType": "ip_domain",
                    "BackupOrigin": ""
                }
            }
        ]
    }
}
```

