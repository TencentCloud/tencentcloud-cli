**Example 1: 查询域名基本信息**



Input: 

```
tccli cdn DescribeDomains --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "64085ba1-4f77-437c-824d-55a188ab1386",
        "Domains": [
            {
                "Area": "mainland",
                "Cname": "www.test.com.cdn.dnsv1.com",
                "CreateTime": "2019-11-15 15:20:46",
                "Disable": "normal",
                "Domain": "www.test.com",
                "Product": "cdn",
                "ParentHost": "",
                "Origin": {
                    "Origins": [
                        "test-1251000004.cos.ap-chengdu.myqcloud.com"
                    ],
                    "OriginType": "cos",
                    "ServerName": "test-1251000004.cos.ap-chengdu.myqcloud.com",
                    "CosPrivateAccess": "off",
                    "OriginPullProtocol": "http",
                    "BackupOrigins": [],
                    "BackupOriginType": null,
                    "BackupServerName": null
                },
                "ProjectId": 0,
                "Readonly": "normal",
                "ResourceId": "cdn-knocwo77",
                "ServiceType": "web",
                "Status": "offline",
                "UpdateTime": "2019-12-04 11:13:09"
            }
        ],
        "TotalNumber": 201
    }
}
```

