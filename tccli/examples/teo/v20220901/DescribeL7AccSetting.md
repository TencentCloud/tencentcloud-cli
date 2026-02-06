**Example 1: 查询七层加速站点配置**

查询站点加速全局配置信息。

Input: 

```
tccli teo DescribeL7AccSetting --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee
```

Output: 
```
{
    "Response": {
        "RequestId": "88215c08-67de-4c7d-974e-a14461816f5b",
        "ZoneSetting": {
            "ZoneName": "example.com",
            "ZoneConfig": {
                "SmartRouting": {
                    "Switch": "off"
                },
                "Cache": {
                    "CustomTime": {
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
                "MaxAge": {
                    "FollowOrigin": "on",
                    "CacheTime": 600
                },
                "CacheKey": {
                    "FullURLCache": "on",
                    "IgnoreCase": "off",
                    "QueryString": {
                        "Action": "includeCustom",
                        "Switch": "off",
                        "Values": []
                    }
                },
                "CachePrefresh": {
                    "CacheTimePercent": 90,
                    "Switch": "off"
                },
                "OfflineCache": {
                    "Switch": "on"
                },
                "Compression": {
                    "Algorithms": [
                        "brotli",
                        "gzip"
                    ],
                    "Switch": "on"
                },
                "ForceRedirectHTTPS": {
                    "RedirectStatusCode": 302,
                    "Switch": "off"
                },
                "HSTS": {
                    "IncludeSubDomains": "off",
                    "Timeout": 0,
                    "Preload": "off",
                    "Switch": "off"
                },
                "TLSConfig": {
                    "Version": [
                        "TLSv1",
                        "TLSv1.1",
                        "TLSv1.2",
                        "TLSv1.3"
                    ],
                    "CipherSuite": "loose-v2023"
                },
                "OCSPStapling": {
                    "Switch": "off"
                },
                "HTTP2": {
                    "Switch": "off"
                },
                "QUIC": {
                    "Switch": "off"
                },
                "UpstreamHTTP2": {
                    "Switch": "off"
                },
                "IPv6": {
                    "Switch": "off"
                },
                "WebSocket": {
                    "Switch": "off",
                    "Timeout": 30
                },
                "PostMaxSize": {
                    "MaxSize": 524288000,
                    "Switch": "on"
                },
                "ClientIPHeader": {
                    "HeaderName": "",
                    "Switch": "off"
                },
                "ClientIPCountry": {
                    "HeaderName": "",
                    "Switch": "off"
                },
                "Grpc": {
                    "Switch": "off"
                },
                "NetworkErrorLogging": {
                    "Switch": "on"
                },
                "AccelerateMainland": {
                    "Switch": "off"
                },
                "StandardDebug": {
                    "AllowClientIPList": [],
                    "Expires": "1969-12-31T16:00:00Z",
                    "Switch": "off"
                }
            }
        }
    }
}
```

