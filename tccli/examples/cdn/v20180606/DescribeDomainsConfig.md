**Example 1: 查询域名详细配置**



Input: 

```
tccli cdn DescribeDomainsConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "07f7dd0b-3936-4bdb-9a85-92b4e20d1b03",
        "Domains": [
            {
                "AccessControl": {
                    "Switch": "off",
                    "AccessControlRules": [],
                    "ReturnCode": 403
                },
                "AccessPort": [
                    80,
                    8080,
                    443
                ],
                "Advance": "on",
                "AdvanceSet": [
                    {
                        "Name": "edge",
                        "Value": "on"
                    },
                    {
                        "Name": "last",
                        "Value": "off"
                    },
                    {
                        "Name": "full",
                        "Value": "off"
                    },
                    {
                        "Name": "quic",
                        "Value": "off"
                    }
                ],
                "AdvancedAuthentication": {
                    "Switch": "off",
                    "TypeA": null,
                    "TypeB": null,
                    "TypeC": null,
                    "TypeD": null,
                    "TypeE": null,
                    "TypeF": null
                },
                "AppId": 123456789,
                "Area": "global",
                "Authentication": {
                    "Switch": "off",
                    "TypeA": null,
                    "TypeB": null,
                    "TypeC": null,
                    "TypeD": null
                },
                "AwsPrivateAccess": {
                    "Switch": "off",
                    "AccessKey": "",
                    "SecretKey": ""
                },
                "BandwidthAlert": {
                    "Switch": "off",
                    "BpsThreshold": 10000000000,
                    "CounterMeasure": "RETURN_404",
                    "LastTriggerTime": null
                },
                "Cache": {
                    "RuleCache": [
                        {
                            "CacheConfig": {
                                "Cache": {
                                    "CacheTime": 86400,
                                    "CompareMaxAge": "off",
                                    "IgnoreCacheControl": "off",
                                    "IgnoreSetCookie": "off",
                                    "Switch": "on"
                                },
                                "NoCache": {
                                    "Switch": "off",
                                    "Revalidate": "off"
                                },
                                "FollowOrigin": {
                                    "Switch": "off"
                                }
                            },
                            "RulePaths": [
                                "*"
                            ],
                            "RuleType": "all"
                        }
                    ],
                    "SimpleCache": null,
                    "AdvancedCache": null
                },
                "CacheKey": {
                    "FullUrlCache": "off",
                    "CacheTag": {
                        "Switch": "off",
                        "Value": null
                    },
                    "Cookie": {
                        "Switch": "off",
                        "Value": ""
                    },
                    "Header": {
                        "Switch": "off",
                        "Value": ""
                    },
                    "IgnoreCase": "off",
                    "KeyRules": [
                        {
                            "FullUrlCache": "on",
                            "IgnoreCase": "off",
                            "QueryString": {
                                "Switch": "off",
                                "Action": null,
                                "Value": ""
                            },
                            "RulePaths": [
                                ".1"
                            ],
                            "RuleType": "file",
                            "RuleTag": "user"
                        }
                    ],
                    "QueryString": {
                        "Switch": "off",
                        "Reorder": "off",
                        "Action": null,
                        "Value": ""
                    },
                    "Scheme": {
                        "Switch": "off"
                    }
                },
                "Cname": "www.test.com.cdn.dnsv1.com",
                "Compatibility": {
                    "Code": 0
                },
                "Compression": {
                    "Switch": "on",
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
                "CreateTime": "2020-12-14 21:14:36",
                "Disable": "normal",
                "Domain": "www.test.com",
                "DownstreamCapping": {
                    "Switch": "off",
                    "CappingRules": []
                },
                "ErrorPage": {
                    "Switch": "off",
                    "PageRules": []
                },
                "FollowRedirect": {
                    "Switch": "off"
                },
                "ForceRedirect": {
                    "Switch": "off",
                    "RedirectType": "http",
                    "RedirectStatusCode": 302,
                    "CarryHeaders": "off"
                },
                "Https": {
                    "Switch": "off",
                    "Http2": "off",
                    "Spdy": "off",
                    "OcspStapling": "off",
                    "VerifyClient": "off",
                    "CertInfo": null,
                    "ClientCertInfo": null,
                    "TlsVersion": [
                        "TLSv1",
                        "TLSv1.1",
                        "TLSv1.2"
                    ],
                    "Hsts": {
                        "Switch": "off",
                        "MaxAge": 0,
                        "IncludeSubDomains": "off"
                    },
                    "SslStatus": "closed"
                },
                "ImageOptimization": {
                    "WebpAdapter": {
                        "Switch": "off"
                    },
                    "TpgAdapter": {
                        "Switch": "off"
                    },
                    "GuetzliAdapter": {
                        "Switch": "off"
                    }
                },
                "IpFilter": {
                    "Switch": "off",
                    "FilterType": "blacklist",
                    "Filters": [],
                    "FilterRules": []
                },
                "IpFreqLimit": {
                    "Switch": "off",
                    "Qps": null
                },
                "Ipv6": {
                    "Switch": "off"
                },
                "Ipv6Access": {
                    "Switch": "off"
                },
                "MaxAge": {
                    "MaxAgeRules": [
                        {
                            "MaxAgeType": "all",
                            "MaxAgeContents": [
                                "*"
                            ],
                            "MaxAgeTime": 0,
                            "FollowOrigin": "on"
                        }
                    ],
                    "Switch": "on"
                },
                "OfflineCache": {
                    "Switch": "off"
                },
                "Origin": {
                    "Origins": [
                        "1.1.1.1"
                    ],
                    "OriginType": "ip",
                    "ServerName": "www.a.com",
                    "CosPrivateAccess": "off",
                    "OriginPullProtocol": "http",
                    "BackupOrigins": [
                        "2.2.2.2"
                    ],
                    "BackupOriginType": "ip",
                    "BackupServerName": "www.a.com",
                    "PathRules": [],
                    "BasePath": null,
                    "PathBasedOrigin": [],
                    "Sni": {
                        "Switch": "off",
                        "ServerName": null
                    }
                },
                "OriginAuthentication": null,
                "OriginCombine": {
                    "Switch": "off"
                },
                "OriginPullOptimization": {
                    "Switch": "off",
                    "OptimizationType": ""
                },
                "OriginPullTimeout": {
                    "ConnectTimeout": 5,
                    "ReceiveTimeout": 10
                },
                "PostMaxSize": {
                    "Switch": "off",
                    "MaxSize": 33554432
                },
                "ProjectId": 0,
                "Quic": {
                    "Switch": "off"
                },
                "RangeOriginPull": {
                    "Switch": "off"
                },
                "Readonly": "normal",
                "Referer": {
                    "Switch": "off",
                    "RefererRules": [
                        {
                            "RuleType": "all",
                            "RulePaths": [
                                "*"
                            ],
                            "RefererType": "whitelist",
                            "Referers": [
                                "1.1.1.1"
                            ],
                            "AllowEmpty": false
                        }
                    ]
                },
                "RequestHeader": {
                    "Switch": "off",
                    "HeaderRules": []
                },
                "ResourceId": "cdn-5ndlcoas",
                "ResponseHeader": {
                    "HeaderRules": [],
                    "Switch": "off"
                },
                "ResponseHeaderCache": {
                    "Switch": "on"
                },
                "SecurityConfig": {
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
                "Status": "online",
                "StatusCodeCache": {
                    "CacheRules": [
                        {
                            "StatusCode": "403",
                            "CacheTime": 0
                        }
                    ],
                    "Switch": "on"
                },
                "Tag": [
                    {
                        "TagKey": "testfornewtag",
                        "TagValue": "brandnew"
                    },
                    {
                        "TagKey": "zzz",
                        "TagValue": "aaa"
                    }
                ],
                "UpdateTime": "2021-03-16 21:04:04",
                "UrlRedirect": {
                    "Switch": "off",
                    "PathRules": []
                },
                "UserAgentFilter": {
                    "Switch": "off",
                    "FilterRules": []
                },
                "VideoSeek": {
                    "Switch": "off"
                },
                "OssPrivateAccess": null,
                "WebSocket": null,
                "RemoteAuthentication": null,
                "ShareCname": null,
                "ParentHost": null,
                "RuleEngine": null
            }
        ],
        "TotalNumber": 1
    }
}
```

