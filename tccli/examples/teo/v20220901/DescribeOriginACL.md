**Example 1: 查询源站防护详情**

查询 ZoneId 为 'zone-276zs184g93m' 的站点使用的七层加速域名/四层代理实例与回源 IP 网段的绑定关系，以及回源 IP 网段详情。

Input: 

```
tccli teo DescribeOriginACL --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m
```

Output: 
```
{
    "Response": {
        "RequestId": "de0a2b4f-df6d-4d2a-ac39-1706cbf8a797",
        "OriginACLInfo": {
            "L7Hosts": [
                "www.example.com"
            ],
            "L4ProxyIds": [
                "proxy-19389e5dwwxfs"
            ],
            "CurrentOriginACL": {
                "EntireAddresses": {
                    "IPv4": [
                        "11.11.11.11/24"
                    ],
                    "IPv6": [
                        "2001:980:7002:6::/64"
                    ]
                },
                "Version": "mlc-1.0.1-20250421",
                "ActiveTime": "2014-11-30T10:00:00Z",
                "IsPlaned": "false"
            },
            "Status": "online",
            "NextOriginACL": {
                "Version": "mlc-1.0.1-20250422",
                "PlannedActiveTime": "2014-12-30T10:00:00Z",
                "EntireAddresses": {
                    "IPv4": [
                        "11.11.11.11/24",
                        "22.22.22.22/24"
                    ],
                    "IPv6": [
                        "2001:980:7002:6::/64"
                    ]
                },
                "AddedAddresses": {
                    "IPv4": [
                        "22.22.22.22/24"
                    ],
                    "IPv6": []
                },
                "RemovedAddresses": {
                    "IPv4": [],
                    "IPv6": []
                },
                "NoChangeAddresses": {
                    "IPv4": [
                        "11.11.11.11/24"
                    ],
                    "IPv6": [
                        "2001:980:7002:6::/64"
                    ]
                }
            }
        }
    }
}
```

