**Example 1: 查询站点下所有安全 IP 分组的配置信息**

查询指定站点的所有安全 IP 分组的配置信息。

Input: 

```
tccli teo DescribeSecurityIPGroup --cli-unfold-argument  \
    --ZoneId zone-nqicqhasui
```

Output: 
```
{
    "Response": {
        "IPGroups": [
            {
                "GroupId": 97,
                "Name": "ExampleIpGroup",
                "Content": [
                    "2.2.2.2",
                    "23.23.23.0/24"
                ],
                "IPExpireInfo": [
                    {
                        "ExpireTime": "2026-03-24T16:03:00+08:00",
                        "IPList": [
                            "2.2.2.2"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

**Example 2: 查询指定 ID 的安全 IP 分组的配置信息**

查询站点中指定 ID 的安全 IP 分组配置信息

Input: 

```
tccli teo DescribeSecurityIPGroup --cli-unfold-argument  \
    --ZoneId zone-ncacqeabax \
    --GroupIds 100 200
```

Output: 
```
{
    "Response": {
        "IPGroups": [
            {
                "GroupId": 100,
                "Name": "ExampleIpGroup-1",
                "Content": [
                    "2.2.2.2",
                    "23.23.23.0/24"
                ],
                "IPExpireInfo": [
                    {
                        "ExpireTime": "2026-03-24T16:03:00+08:00",
                        "IPList": [
                            "2.2.2.2"
                        ]
                    }
                ]
            },
            {
                "GroupId": 200,
                "Name": "ExampleIpGroup-2",
                "Content": [
                    "1.1.1.1",
                    "23.23.23.0/24"
                ],
                "IPExpireInfo": [
                    {
                        "ExpireTime": "2025-03-24T16:03:00+08:00",
                        "IPList": [
                            "1.1.1.1"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

