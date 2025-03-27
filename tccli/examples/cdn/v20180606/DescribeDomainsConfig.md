**Example 1: 查询域名详细配置**



Input: 

```
tccli cdn DescribeDomainsConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name domainType \
    --Filters.0.Value cname
```

Output: 
```
{
    "Response": {
        "RequestId": "7c152eaf-a4a4-4fc2-8204-c586ad91e8ec",
        "Domains": [
            {
                "AccessControl": {
                    "AccessControlRules": [],
                    "ReturnCode": 403,
                    "Switch": "off"
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
                        "Value": "on"
                    },
                    {
                        "Name": "full",
                        "Value": "on"
                    },
                    {
                        "Name": "quic",
                        "Value": "on"
                    },
                    {
                        "Name": "staging",
                        "Value": "off"
                    },
                    {
                        "Name": "tes_staging",
                        "Value": "off"
                    },
                    {
                        "Name": "overdue_offline_https",
                        "Value": "off"
                    },
                    {
                        "Name": "overdue_offline_apk",
                        "Value": "off"
                    },
                    {
                        "Name": "overdue_offline_quic",
                        "Value": "off"
                    },
                    {
                        "Name": "overdue_offline_single_area",
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
                "AppId": 12345,
                "Area": "mainland",
                "Authentication": {
                    "AuthAlgorithm": "md5",
                    "Switch": "off",
                    "TypeA": null,
                    "TypeB": null,
                    "TypeC": null,
                    "TypeD": null
                },
                "AwsPrivateAccess": {
                    "AccessKey": null,
                    "Bucket": null,
                    "Region": null,
                    "SecretKey": null,
                    "Switch": "off"
                },
                "BandwidthAlert": {
                    "AlertPercentage": 80,
                    "AlertSwitch": "off",
                    "BpsThreshold": 10000000000,
                    "CounterMeasure": "RETURN_404",
                    "LastTriggerTime": null,
                    "LastTriggerTimeOverseas": null,
                    "Metric": "bandwidth",
                    "StatisticItems": [],
                    "Switch": "off"
                },
                "Cache": {
                    "AdvancedCache": null,
                    "RuleCache": null,
                    "SimpleCache": {
                        "CacheRules": [
                            {
                                "CacheContents": [
                                    "/data"
                                ],
                                "CacheTime": 2592000,
                                "CacheType": "all"
                            },
                            {
                                "CacheContents": [
                                    "php",
                                    "jsp",
                                    "asp",
                                    "aspx"
                                ],
                                "CacheTime": 0,
                                "CacheType": "file"
                            }
                        ],
                        "CompareMaxAge": "off",
                        "FollowOrigin": "off",
                        "IgnoreCacheControl": "off",
                        "IgnoreSetCookie": "off",
                        "Revalidate": {
                            "Path": "/data",
                            "Switch": "off"
                        }
                    }
                },
                "CacheKey": {
                    "CacheTag": {
                        "Switch": "off",
                        "Value": null
                    },
                    "Cookie": {
                        "Switch": "off",
                        "Value": ""
                    },
                    "FullUrlCache": "on",
                    "Header": {
                        "Switch": "off",
                        "Value": ""
                    },
                    "IgnoreCase": "off",
                    "KeyRules": [],
                    "QueryString": {
                        "Action": null,
                        "Reorder": "off",
                        "Switch": "off",
                        "Value": ""
                    },
                    "Scheme": {
                        "Switch": "off"
                    }
                },
                "Cname": "qq.com.cdntest.cdn.dnsv1.com",
                "Compatibility": {
                    "Code": 0
                },
                "Compression": {
                    "CompressionRules": [
                        {
                            "Algorithms": [
                                "gzip"
                            ],
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
                            "MaxLength": 2097152,
                            "MinLength": 256,
                            "RulePaths": [],
                            "RuleType": null
                        }
                    ],
                    "Switch": "on"
                },
                "CreateTime": "2024-12-18 14:29:28",
                "Disable": "normal",
                "Domain": "qq.com",
                "DownstreamCapping": {
                    "CappingRules": [],
                    "Switch": "off"
                },
                "ErrorPage": {
                    "PageRules": [],
                    "Switch": "off"
                },
                "FollowRedirect": {
                    "RedirectConfig": {
                        "FollowRedirectBackupHost": "",
                        "FollowRedirectHost": "",
                        "Switch": "off"
                    },
                    "Switch": "off"
                },
                "ForceRedirect": {
                    "CarryHeaders": "off",
                    "RedirectStatusCode": 302,
                    "RedirectType": "http",
                    "Switch": "off"
                },
                "Https": {
                    "CertInfo": null,
                    "ClientCertInfo": null,
                    "Hsts": {
                        "IncludeSubDomains": "off",
                        "MaxAge": 0,
                        "Switch": "off"
                    },
                    "Http2": "off",
                    "OcspStapling": "off",
                    "Spdy": "off",
                    "Switch": "off",
                    "TlsVersion": [
                        "TLSv1",
                        "TLSv1.1",
                        "TLSv1.2",
                        "TLSv1.3"
                    ],
                    "VerifyClient": "off",
                    "SslStatus": "closed"
                },
                "HttpsBilling": {
                    "Switch": "off"
                },
                "HwPrivateAccess": {
                    "AccessKey": null,
                    "Bucket": null,
                    "SecretKey": null,
                    "Switch": "off"
                },
                "ImageOptimization": {
                    "AvifAdapter": {
                        "FallbackFormats": [],
                        "Switch": "off"
                    },
                    "GuetzliAdapter": {
                        "Switch": "off"
                    },
                    "TpgAdapter": {
                        "Switch": "off"
                    },
                    "WebpAdapter": {
                        "Switch": "off"
                    }
                },
                "IpFilter": {
                    "FilterRules": [],
                    "FilterType": "blacklist",
                    "Filters": [],
                    "ReturnCode": 514,
                    "Switch": "off"
                },
                "IpFreqLimit": {
                    "Qps": null,
                    "Switch": "off"
                },
                "Ipv6": {
                    "Switch": "on"
                },
                "Ipv6Access": {
                    "Switch": "off"
                },
                "MaxAge": {
                    "MaxAgeCodeRule": null,
                    "MaxAgeRules": [],
                    "Switch": "off"
                },
                "OfflineCache": {
                    "Switch": "off"
                },
                "Origin": {
                    "AdvanceHttps": {
                        "CertInfo": null,
                        "Cipher": "DEFAULT",
                        "CustomTlsStatus": "off",
                        "OriginCertInfo": null,
                        "TlsVersion": [
                            "TLSv1",
                            "TLSv1.1",
                            "TLSv1.2",
                            "TLSv1.3"
                        ],
                        "VerifyOriginType": "off"
                    },
                    "BackupOriginType": null,
                    "BackupOrigins": [],
                    "BackupServerName": null,
                    "BasePath": null,
                    "CosPrivateAccess": "off",
                    "OriginCompany": null,
                    "OriginPullProtocol": "http",
                    "OriginType": "domain",
                    "Origins": [
                        "httpbin.org"
                    ],
                    "PathBasedOrigin": [],
                    "PathRules": [],
                    "ServerName": "qq.com",
                    "Sni": {
                        "ServerName": null,
                        "Switch": "off"
                    }
                },
                "OriginAuthentication": {
                    "Switch": "off",
                    "TypeA": null
                },
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
                "OssPrivateAccess": {
                    "AccessKey": null,
                    "Bucket": null,
                    "Region": null,
                    "SecretKey": null,
                    "Switch": "off"
                },
                "OthersPrivateAccess": {
                    "AccessKey": null,
                    "Bucket": null,
                    "Region": null,
                    "SecretKey": null,
                    "Switch": "off"
                },
                "ParamFilter": {
                    "FilterRules": [],
                    "Switch": "off"
                },
                "ParentHost": "",
                "PostMaxSize": {
                    "MaxSize": 33554432,
                    "Switch": "off"
                },
                "ProjectId": 0,
                "QnPrivateAccess": {
                    "AccessKey": "",
                    "SecretKey": "",
                    "Switch": "off"
                },
                "Quic": {
                    "Switch": "off"
                },
                "RangeOriginPull": {
                    "RangeRules": [],
                    "Switch": "on"
                },
                "Readonly": "normal",
                "Referer": {
                    "RefererRules": [],
                    "Switch": "off"
                },
                "RemoteAuthentication": {
                    "RemoteAuthenticationRules": null,
                    "Server": null,
                    "Switch": "off"
                },
                "RequestHeader": {
                    "HeaderRules": [
                        {
                            "HeaderMode": "add",
                            "HeaderName": "Tencent-Acceleration-Domain-Name",
                            "HeaderValue": "$host",
                            "RulePaths": [
                                "/data"
                            ],
                            "RuleType": "all"
                        }
                    ],
                    "Switch": "on"
                },
                "ResourceId": "cdn-clrsr",
                "ResponseHeader": {
                    "HeaderRules": [],
                    "Switch": "off"
                },
                "ResponseHeaderCache": {
                    "Switch": "on"
                },
                "RuleEngine": {
                    "Content": null,
                    "Switch": "off"
                },
                "SecurityConfig": {
                    "Switch": "off"
                },
                "Seo": {
                    "Switch": "off"
                },
                "ServiceType": "web",
                "ShareCname": {
                    "Cname": null,
                    "Switch": "off"
                },
                "SpecificConfig": {
                    "Mainland": null,
                    "Overseas": null
                },
                "Status": "online",
                "StatusCodeCache": {
                    "CacheRules": [
                        {
                            "CacheTime": 10,
                            "StatusCode": "404"
                        }
                    ],
                    "Switch": "on"
                },
                "Tag": null,
                "UpdateTime": "2024-12-18 14:31:34",
                "UrlRedirect": {
                    "PathRules": [],
                    "Switch": "off"
                },
                "UserAgentFilter": {
                    "FilterRules": [],
                    "Switch": "off"
                },
                "VideoSeek": {
                    "Switch": "off"
                },
                "WebSocket": {
                    "Switch": "off",
                    "Timeout": 30
                }
            }
        ],
        "TotalNumber": 1
    }
}
```

