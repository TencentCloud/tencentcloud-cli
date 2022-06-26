**Example 1: 查询站点配置**



Input: 

```
tccli teo DescribeZoneSetting --cli-unfold-argument  \
    --ZoneId zone-xxxx
```

Output: 
```
{
    "Response": {
        "Origin": {
            "OriginPullProtocol": "xx"
        },
        "CacheKey": {
            "FullUrlCache": "xx",
            "IgnoreCase": "xx",
            "QueryString": {
                "Action": "xx",
                "Switch": "xx",
                "Value": [
                    "xx"
                ]
            }
        },
        "WebSocket": {
            "Switch": "xx",
            "Timeout": 0
        },
        "Compression": {
            "Switch": "xx"
        },
        "Zone": "xx",
        "ForceRedirect": {
            "Switch": "xx",
            "RedirectStatusCode": 0
        },
        "Https": {
            "Hsts": {
                "IncludeSubDomains": "xx",
                "Preload": "xx",
                "Switch": "xx",
                "MaxAge": 0
            },
            "OcspStapling": "xx",
            "TlsVersion": [
                "xx"
            ],
            "Http2": "xx"
        },
        "Cache": {
            "FollowOrigin": {
                "Switch": "xx"
            },
            "Cache": {
                "CacheTime": 0,
                "Switch": "xx",
                "IgnoreCacheControl": "xx"
            },
            "NoCache": {
                "Switch": "xx"
            }
        },
        "PostMaxSize": {
            "Switch": "xx",
            "MaxSize": 0
        },
        "MaxAge": {
            "FollowOrigin": "xx",
            "MaxAgeTime": 0
        },
        "ZoneId": "xx",
        "UpstreamHttp2": {
            "Switch": "xx"
        },
        "ClientIpHeader": {
            "HeaderName": "xx",
            "Switch": "xx"
        },
        "OfflineCache": {
            "Switch": "xx"
        },
        "Quic": {
            "Switch": "xx"
        },
        "CachePrefresh": {
            "Switch": "xx",
            "Percent": 0
        },
        "SmartRouting": {
            "Switch": "xx"
        },
        "RequestId": "xx"
    }
}
```

