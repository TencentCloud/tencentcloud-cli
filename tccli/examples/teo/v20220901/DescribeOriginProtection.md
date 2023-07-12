**Example 1: 查询源站防护信息**

查询源站防护信息

Input: 

```
tccli teo DescribeOriginProtection --cli-unfold-argument  \
    --ZoneIds zone-276zs184g93m \
    --Filters.0.Values true \
    --Filters.0.Name need-update \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "de0a2b4f-df6d-4d2a-ac39-1706cbf8a797",
        "OriginProtectionInfo": [
            {
                "ZoneId": "zone-276zs184g93m",
                "Hosts": [
                    "www.qq.com"
                ],
                "ProxyIds": [
                    "proxy-19389e5dwwxfs"
                ],
                "CurrentIPWhitelist": {
                    "IPv4": [
                        "11.11.11.11/24"
                    ],
                    "IPv6": [
                        "2001:980:7002:6::/64"
                    ]
                },
                "NeedUpdate": true,
                "Status": "online",
                "PlanSupport": true,
                "DiffIPWhitelist": {
                    "LatestIPWhitelist": {
                        "IPv4": [
                            "11.11.11.11/24",
                            "22.22.22.22/24"
                        ],
                        "IPv6": [
                            "2001:980:7002:6::/64"
                        ]
                    },
                    "AddedIPWhitelist": {
                        "IPv4": [
                            "22.22.22.22/24"
                        ],
                        "IPv6": []
                    },
                    "RemovedIPWhitelist": {
                        "IPv4": [],
                        "IPv6": []
                    },
                    "NoChangeIPWhitelist": {
                        "IPv4": [
                            "11.11.11.11/24"
                        ],
                        "IPv6": [
                            "2001:980:7002:6::/64"
                        ]
                    }
                }
            }
        ]
    }
}
```

