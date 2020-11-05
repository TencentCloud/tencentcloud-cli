**Example 1: Querying domain name configuration**



Input: 

```
tccli cdn DescribeDomainsConfig --cli-unfold-argument  \
    --Offset 0\
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ba516c05-42d9-49c7-b275-7775be0475ba",
        "Domains": [
            {
                "Area": "mainland",
                "Authentication": {
                    "Switch": "off",
                    "TypeA": null,
                    "TypeB": null,
                    "TypeC": null,
                    "TypeD": null
                },
                "BandwidthAlert": {
                    "Switch": "off",
                    "BpsThreshold": 10000000000,
                    "CounterMeasure": "RETURN_404",
                    "LastTriggerTime": null
                },
                "Cache": {
                    "SimpleCache": {
                        "CacheRules": [
                            {
                                "CacheType": "all",
                                "CacheContents": [
                                    "*"
                                ],
                                "CacheTime": 2592000
                            }
                        ],
                        "IgnoreCacheControl": "off",
                        "IgnoreSetCookie": "off",
                        "CompareMaxAge": "off",
                        "FollowOrigin": "off"
                    },
                    "AdvancedCache": null
                },
                "CacheKey": {
                    "FullUrlCache": "on"
                },
                "Cname": "www.test.com.cdn.dnsv1.com",
                "Compatibility": {
                    "Code": 0
                },
                "Compression": {
                    "Switch": "off",
                    "CompressionRules": [
                        {
                            "Compress": true,
                            "FileExtensions": [
                                "js",
                                "html",
                                "css",
                                "xml",
                                "json",
                                "shtml",
                                "htm"
                            ],
                            "MinLength": 256,
                            "MaxLength": 2097152,
                            "Algorithms": [
                                "gzip"
                            ]
                        }
                    ]
                },
                "CreateTime": "2019-11-15 15:20:46",
                "Disable": "normal",
                "Domain": "www.test.com",
                "DownstreamCapping": {
                    "Switch": "off",
                    "CappingRules": []
                },
                "ErrorPage": {
                    "PageRules": [],
                    "Switch": "off"
                },
                "FollowRedirect": {
                    "Switch": "on"
                },
                "ForceRedirect": {
                    "Switch": "off",
                    "RedirectType": "http",
                    "RedirectStatusCode": 302
                },
                "Https": {
                    "Switch": "off",
                    "Http2": "off",
                    "Spdy": "off",
                    "OcspStapling": "off",
                    "VerifyClient": "off",
                    "CertInfo": null,
                    "ClientCertInfo": null,
                    "SslStatus": "closed"
                },
                "IpFilter": {
                    "Switch": "off",
                    "FilterType": "blacklist",
                    "Filters": []
                },
                "IpFreqLimit": {
                    "Switch": "off",
                    "Qps": null
                },
                "Ipv6": {
                    "Switch": "off"
                },
                "MaxAge": {
                    "MaxAgeRules": [],
                    "Switch": "off"
                },
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
                "OriginPullOptimization": {
                    "Switch": "off",
                    "OptimizationType": ""
                },
                "ProjectId": 0,
                "RangeOriginPull": {
                    "Switch": "on"
                },
                "Readonly": "normal",
                "Referer": {
                    "Switch": "off",
                    "RefererRules": []
                },
                "RequestHeader": {
                    "HeaderRules": [],
                    "Switch": "off"
                },
                "ResourceId": "cdn-knocwo77",
                "ResponseHeader": {
                    "HeaderRules": [],
                    "Switch": "off"
                },
                "ResponseHeaderCache": {
                    "Switch": "off"
                },
                "Seo": {
                    "Switch": "off"
                },
                "ServiceType": "web",
                "SpecificConfig": {
                    "Mainland": null,
                    "Overseas": null
                },
                "Status": "offline",
                "StatusCodeCache": {
                    "CacheRules": [
                        {
                            "StatusCode": "404",
                            "CacheTime": 10
                        }
                    ],
                    "Switch": "on"
                },
                "UpdateTime": "2019-12-04 11:13:09",
                "VideoSeek": {
                    "Switch": "off"
                }
            }
        ],
        "TotalNumber": 201
    }
}
```

