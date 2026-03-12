**Example 1: 查询域名基本信息**



Input: 

```
tccli cdn DescribeDomainsForCos --cli-unfold-argument  \
    --Origins testcdn-1252662529.cos.ap-nanjing.myqcloud.com
```

Output: 
```
{
    "Response": {
        "Domains": [
            {
                "AppId": 1300295767,
                "Area": "mainland",
                "Cname": "**************************.com.cdn.dnsv1.com",
                "CreateTime": "2025-12-30 16:49:23",
                "Disable": "normal",
                "Domain": "**************************.com",
                "MigrateEo": 0,
                "Origin": {
                    "OriginType": "cos",
                    "Origins": [
                        "testcdn-1252662529.cos.ap-nanjing.myqcloud.com"
                    ],
                    "ServerName": "testcdn-1252662529.cos.ap-nanjing.myqcloud.com"
                },
                "ParentHost": "",
                "Product": "cdn",
                "ProjectId": 0,
                "Readonly": "normal",
                "ResourceId": "cdn-k3c7s0z5",
                "ServiceType": "web",
                "Status": "online",
                "UpdateTime": "2026-01-26 19:23:34"
            }
        ],
        "TotalNumber": 2,
        "RequestId": "2b42d487-cd4d-419c-bae8-40d474ad6176"
    }
}
```

