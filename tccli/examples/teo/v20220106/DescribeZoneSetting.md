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
        "RequestId": "ddc589b3-c3f3-487d-a29e-43a9008d3c59",
        "Area": "mainland",
        "Cache": {
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
        "CachePrefresh": {
            "Percent": 90,
            "Switch": "off"
        },
        "ClientIpHeader": {
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
        "Https": {
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
            "OriginPullProtocol": "follow"
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
        "UpstreamHttp2": {
            "Switch": "off"
        },
        "WebSocket": {
            "Switch": "off",
            "Timeout": 30
        },
        "Zone": "test.com",
        "ZoneId": "zone-21xfqlh4qjee"
    }
}
```

