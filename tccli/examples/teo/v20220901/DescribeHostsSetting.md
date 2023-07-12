**Example 1: 查询域名详细配置**



Input: 

```
tccli teo DescribeHostsSetting --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16
```

Output: 
```
{
    "Response": {
        "DetailHosts": [
            {
                "Status": "online",
                "Host": "test.example.com",
                "ZoneId": "zone-27q0p0bali16",
                "ZoneName": "example.com",
                "Cname": "test.example.com.acc.edgeonedy1.com.",
                "Id": "edge-ja6yyfjh",
                "InstanceId": "edge-ja6yyfjh",
                "Lock": 0,
                "Mode": 0,
                "Area": "mainland",
                "AccelerateType": {
                    "Switch": "on"
                },
                "CacheConfig": {
                    "Cache": {
                        "CacheTime": 2592000,
                        "Switch": "off"
                    },
                    "FollowOrigin": {
                        "Switch": "on"
                    },
                    "NoCache": {
                        "Switch": "off"
                    }
                },
                "CacheKey": {
                    "FullUrlCache": "on",
                    "IgnoreCase": "off",
                    "QueryString": {
                        "Action": "includeCustom",
                        "Switch": "off",
                        "Value": []
                    }
                },
                "Compression": {
                    "Algorithms": [
                        "brotli",
                        "gzip"
                    ],
                    "Switch": "on"
                },
                "DDoS": {
                    "Switch": "on"
                },
                "CC": {
                    "PolicyId": 1996,
                    "Switch": "on"
                },
                "Waf": {
                    "PolicyId": 1995,
                    "Switch": "on"
                },
                "Https": {
                    "CertInfo": [],
                    "Hsts": {
                        "IncludeSubDomains": "off",
                        "MaxAge": 1,
                        "Preload": "off",
                        "Switch": "on"
                    },
                    "Http2": "on",
                    "OcspStapling": "off",
                    "TlsVersion": [
                        "TLSv1",
                        "TLSv1.1",
                        "TLSv1.2",
                        "TLSv1.3"
                    ]
                },
                "Ipv6": {
                    "Switch": "off"
                },
                "Origin": {
                    "BackupOrigins": [],
                    "CosPrivateAccess": "off",
                    "OriginPullProtocol": "follow",
                    "Origins": [
                        "1.1.1.1:80:100"
                    ]
                },
                "SecurityType": {
                    "Switch": "on"
                },
                "SmartRouting": {
                    "Switch": "off"
                }
            }
        ],
        "RequestId": "9cc50b24-7dc5-44f4-96ce-95825d53ff2f",
        "TotalNumber": 1
    }
}
```

