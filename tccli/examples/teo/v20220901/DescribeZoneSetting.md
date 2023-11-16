**Example 1: 查询站点配置**



Input: 

```
tccli teo DescribeZoneSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee
```

Output: 
```
{
    "Response": {
        "RequestId": "88215c08-67de-4c7d-974e-a14461816f5b",
        "ZoneSetting": {
            "AccelerateMainland": {
                "Switch": "off"
            },
            "Area": "global",
            "CacheConfig": {
                "Cache": {
                    "CacheTime": 2592000,
                    "Switch": "off"
                },
                "FollowOrigin": {
                    "DefaultCache": "on",
                    "DefaultCacheStrategy": "on",
                    "DefaultCacheTime": 0,
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
            "CachePrefresh": {
                "Percent": 90,
                "Switch": "off"
            },
            "ClientIpCountry": {
                "HeaderName": "",
                "Switch": "off"
            },
            "ClientIpHeader": {
                "HeaderName": "",
                "Switch": "off"
            },
            "Compression": {
                "Algorithms": [
                    "brotli",
                    "gzip"
                ],
                "Switch": "on"
            },
            "ForceRedirect": {
                "RedirectStatusCode": 302,
                "Switch": "off"
            },
            "Grpc": {
                "Switch": "off"
            },
            "Https": {
                "ApplyType": "none",
                "CertInfo": [],
                "CipherSuite": "loose-v2023",
                "Hsts": {
                    "IncludeSubDomains": "off",
                    "MaxAge": 0,
                    "Preload": "off",
                    "Switch": "off"
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
            "ImageOptimize": {
                "Switch": "off"
            },
            "Ipv6": {
                "Switch": "off"
            },
            "MaxAge": {
                "FollowOrigin": "on",
                "MaxAgeTime": 600
            },
            "OfflineCache": {
                "Switch": "on"
            },
            "Origin": {
                "Origins": [
                    "30.12.34.23"
                ],
                "BackupOrigins": [
                    "30.12.34.11"
                ],
                "OriginPullProtocol": "follow",
                "CosPrivateAccess": "abc"
            },
            "PostMaxSize": {
                "MaxSize": 524288000,
                "Switch": "on"
            },
            "Quic": {
                "Switch": "off"
            },
            "SmartRouting": {
                "Switch": "off"
            },
            "StandardDebug": {
                "AllowClientIPList": [],
                "ExpireTime": "1969-12-31T16:00:00Z",
                "Switch": "off"
            },
            "UpstreamHttp2": {
                "Switch": "off"
            },
            "WebSocket": {
                "Switch": "off",
                "Timeout": 30
            },
            "ZoneName": "wxlagame.com"
        }
    }
}
```

