**Example 1: 查询域名简要信息**



Input: 

```
tccli ecdn DescribeDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "104fcdb5-293c-4f6f-b63d-0c9e430264e3",
        "Domains": [
            {
                "AppId": 1251000000,
                "Area": "mainland",
                "Cname": "test.com.dsa.dnsv1.com",
                "CreateTime": "2019-12-03 15:23:50",
                "Disable": "normal",
                "Domain": "test.com",
                "Tag": [],
                "Origin": {
                    "Origins": [
                        "1.1.1.1"
                    ],
                    "OriginType": "ip",
                    "ServerName": null,
                    "OriginPullProtocol": "http",
                    "BackupOrigins": [],
                    "BackupOriginType": null
                },
                "ProjectId": 0,
                "Readonly": "normal",
                "ResourceId": "ecdn-xxxx",
                "Status": "processing",
                "UpdateTime": "2019-12-03 15:23:50"
            }
        ],
        "TotalCount": 10
    }
}
```

