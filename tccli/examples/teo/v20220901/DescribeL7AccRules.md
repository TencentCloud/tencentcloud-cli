**Example 1: 查询规则引擎规则列表**

查询规则引擎规则列表。

Input: 

```
tccli teo DescribeL7AccRules --cli-unfold-argument  \
    --ZoneId zone-27q0p0lali12
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Rules": [
            {
                "RuleName": "测试规则",
                "Status": "disable",
                "RuleId": "rule-djuq23",
                "Description": [
                    "注释 1",
                    "注释 2"
                ],
                "Branches": [
                    {
                        "Condition": "${http.request.host} in ['www.example.com']",
                        "Actions": [
                            {
                                "Name": "ModifyOrigin",
                                "ModifyOriginParameters": {
                                    "OriginType": "IPDomain",
                                    "Origin": "1.1.1.1",
                                    "OriginProtocol": "follow",
                                    "HTTPOriginPort": 80,
                                    "HTTPSOriginPort": 443
                                }
                            }
                        ],
                        "SubRules": [
                            {
                                "Description": [
                                    "节点缓存TTL示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "Cache",
                                                "CacheParameters": {
                                                    "FollowOrigin": {
                                                        "Switch": "on",
                                                        "DefaultCache": "on",
                                                        "DefaultCacheStrategy": "on",
                                                        "DefaultCacheTime": 0
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "浏览器缓存TTL示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "MaxAge",
                                                "MaxAgeParameters": {
                                                    "FollowOrigin": "off",
                                                    "CacheTime": 0
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "自定义CacheKey示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "CacheKey",
                                                "CacheKeyParameters": {
                                                    "FullURLCache": "off",
                                                    "QueryString": {
                                                        "Switch": "on",
                                                        "Action": "includeCustom",
                                                        "Values": [
                                                            "name1",
                                                            "name2"
                                                        ]
                                                    },
                                                    "IgnoreCase": "on",
                                                    "Header": {
                                                        "Switch": "on",
                                                        "Values": [
                                                            "EO-Client-Device",
                                                            "EO-Client-OS"
                                                        ]
                                                    },
                                                    "Scheme": "on",
                                                    "Cookie": {
                                                        "Switch": "off"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "状态码缓存TTL示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "StatusCodeCache",
                                                "StatusCodeCacheParameters": {
                                                    "StatusCodeCacheParams": [
                                                        {
                                                            "StatusCode": 400,
                                                            "CacheTime": 4
                                                        },
                                                        {
                                                            "StatusCode": 401,
                                                            "CacheTime": 180
                                                        },
                                                        {
                                                            "StatusCode": 403,
                                                            "CacheTime": 7200
                                                        },
                                                        {
                                                            "StatusCode": 404,
                                                            "CacheTime": 86400
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "缓存预刷新示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "CachePrefresh",
                                                "CachePrefreshParameters": {
                                                    "Switch": "on",
                                                    "CacheTimePercent": 80
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "离线缓存示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "OfflineCache",
                                                "OfflineCacheParameters": {
                                                    "Switch": "on"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "HTTP2示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "HTTP2",
                                                "HTTP2Parameters": {
                                                    "Switch": "on"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "QUIC示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "QUIC",
                                                "QUICParameters": {
                                                    "Switch": "on"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "WebSocket示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "WebSocket",
                                                "WebSocketParameters": {
                                                    "Switch": "on",
                                                    "Timeout": 30
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "最大上传大小示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "PostMaxSize",
                                                "PostMaxSizeParameters": {
                                                    "Switch": "on",
                                                    "MaxSize": 524288000
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "智能压缩示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "Compression",
                                                "CompressionParameters": {
                                                    "Switch": "on",
                                                    "Algorithms": [
                                                        "gzip"
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "智能加速示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "SmartRouting",
                                                "SmartRoutingParameters": {
                                                    "Switch": "on"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "HTTP2回源示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "UpstreamHTTP2",
                                                "UpstreamHTTP2Parameters": {
                                                    "Switch": "off"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "回源超时时间示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "HTTPUpstreamTimeout",
                                                "HTTPUpstreamTimeoutParameters": {
                                                    "ResponseTimeout": 15
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "强制 HTTPS示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "ForceRedirectHTTPS",
                                                "ForceRedirectHTTPSParameters": {
                                                    "Switch": "on",
                                                    "RedirectStatusCode": 302
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "HSTS示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "HSTS",
                                                "HSTSParameters": {
                                                    "Switch": "on",
                                                    "Timeout": 1000,
                                                    "IncludeSubDomains": "on",
                                                    "Preload": "on"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "SSL/TLS 安全配置示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "TLSConfig",
                                                "TLSConfigParameters": {
                                                    "Version": [
                                                        "TLSv1",
                                                        "TLSv1.1",
                                                        "TLSv1.2",
                                                        "TLSv1.3"
                                                    ],
                                                    "CipherSuite": "loose-v2023"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "OCSP 装订示例",
                                    "回源请求参数设置示例",
                                    "回源跟随重定向示例",
                                    "自定义错误页面示例",
                                    "分片回源示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "OCSPStapling",
                                                "OCSPStaplingParameters": {
                                                    "Switch": "on"
                                                }
                                            },
                                            {
                                                "Name": "UpstreamRequest",
                                                "UpstreamRequestParameters": {
                                                    "QueryString": {
                                                        "Switch": "on",
                                                        "Action": "includeCustom",
                                                        "Values": [
                                                            "name1",
                                                            "name2"
                                                        ]
                                                    },
                                                    "Cookie": {
                                                        "Switch": "on",
                                                        "Action": "full"
                                                    }
                                                }
                                            },
                                            {
                                                "Name": "UpstreamFollowRedirect",
                                                "UpstreamFollowRedirectParameters": {
                                                    "Switch": "on",
                                                    "MaxTimes": 3
                                                }
                                            },
                                            {
                                                "Name": "ErrorPage",
                                                "ErrorPageParameters": {
                                                    "ErrorPageParams": [
                                                        {
                                                            "StatusCode": 400,
                                                            "RedirectURL": "http://www.test-v.com/custom-page.html"
                                                        },
                                                        {
                                                            "StatusCode": 403,
                                                            "RedirectURL": "http://www.test-v.com/custom-page1.html"
                                                        }
                                                    ]
                                                }
                                            },
                                            {
                                                "Name": "RangeOriginPull",
                                                "RangeOriginPullParameters": {
                                                    "Switch": "on"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "回源 HTTPS示例",
                                    "修改 HTTP 回源请求头示例",
                                    "Host Header 重写示例",
                                    "访问 URL 重定向示例",
                                    "Token 鉴权示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "OriginPullProtocol"
                                            },
                                            {
                                                "Name": "ModifyRequestHeader",
                                                "ModifyRequestHeaderParameters": {
                                                    "HeaderActions": [
                                                        {
                                                            "Action": "add",
                                                            "Name": "EO-Client-Browser"
                                                        },
                                                        {
                                                            "Action": "del",
                                                            "Name": "EO-Client-Device"
                                                        },
                                                        {
                                                            "Action": "set",
                                                            "Name": "EO-Client-OS"
                                                        }
                                                    ]
                                                }
                                            },
                                            {
                                                "Name": "HostHeader",
                                                "HostHeaderParameters": {
                                                    "Action": "followOrigin"
                                                }
                                            },
                                            {
                                                "Name": "AccessURLRedirect",
                                                "AccessURLRedirectParameters": {
                                                    "StatusCode": 302,
                                                    "Protocol": "follow",
                                                    "HostName": {
                                                        "Action": "follow"
                                                    },
                                                    "URLPath": {
                                                        "Action": "follow"
                                                    },
                                                    "QueryString": {
                                                        "Action": "full"
                                                    }
                                                }
                                            },
                                            {
                                                "Name": "Authentication",
                                                "AuthenticationParameters": {
                                                    "AuthType": "TypeA",
                                                    "Timeout": 5,
                                                    "SecretKey": "BCChgIM4o0k08Uk0Jgi3f27ir3",
                                                    "BackupSecretKey": "3deJ7O6CsqlIk",
                                                    "AuthParam": "test123QQ"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "Description": [
                                    "修改 HTTP 节点响应头示例",
                                    "客户端 IP 头部示例",
                                    "客户端 IP 地理位置头部示例",
                                    "HTTP 应答示例",
                                    "回源 URL 重写示例"
                                ],
                                "Branches": [
                                    {
                                        "Condition": "${http.request.host} in ['www.example.com']",
                                        "Actions": [
                                            {
                                                "Name": "ModifyResponseHeader",
                                                "ModifyResponseHeaderParameters": {
                                                    "HeaderActions": [
                                                        {
                                                            "Action": "add",
                                                            "Name": "Access-Control-Allow-Methods",
                                                            "Value": "POST,GET"
                                                        },
                                                        {
                                                            "Action": "set",
                                                            "Name": "Access-Control-Allow-Origin",
                                                            "Value": "http://test.com,http://1.1.1.1"
                                                        },
                                                        {
                                                            "Action": "del",
                                                            "Name": "Content-Disposition"
                                                        }
                                                    ]
                                                }
                                            },
                                            {
                                                "Name": "ClientIPHeader",
                                                "ClientIPHeaderParameters": {
                                                    "Switch": "on",
                                                    "HeaderName": "test"
                                                }
                                            },
                                            {
                                                "Name": "ClientIPCountry",
                                                "ClientIPCountryParameters": {
                                                    "Switch": "on",
                                                    "HeaderName": "EO-Client-IPCountry"
                                                }
                                            },
                                            {
                                                "Name": "HttpResponse",
                                                "HttpResponseParameters": {
                                                    "StatusCode": 400,
                                                    "ResponsePage": "p-30tcxgl8i0ls"
                                                }
                                            },
                                            {
                                                "Name": "UpstreamURLRewrite",
                                                "UpstreamURLRewriteParameters": {
                                                    "Type": "Path",
                                                    "Action": "addPrefix",
                                                    "Value": "/prefix"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

