**Example 1: 查询域名详细配置**



Input: 

```
tccli ecdn DescribeDomainsConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "932fe708-0ce1-46ec-b403-bcd8bdb08fdd",
        "Domains": [
            {
                "AppId": 1251000000,
                "Area": "mainland",
                "Cache": {
                    "CacheRules": [
                        {
                            "CacheType": "all",
                            "CacheContents": [
                                "*"
                            ],
                            "CacheTime": 0
                        },
                        {
                            "CacheType": "file",
                            "CacheContents": [
                                "gif",
                                "png",
                                "bmp",
                                "jpg",
                                "jpeg",
                                "mp3",
                                "wma",
                                "flv",
                                "mp4",
                                "wmv",
                                "avi",
                                "m3u8",
                                "ts"
                            ],
                            "CacheTime": 86400
                        },
                        {
                            "CacheType": "file",
                            "CacheContents": [
                                "doc",
                                "docx",
                                "xls",
                                "xlsx",
                                "ppt",
                                "pptx",
                                "txt",
                                "pdf"
                            ],
                            "CacheTime": 86400
                        },
                        {
                            "CacheType": "file",
                            "CacheContents": [
                                "exe",
                                "apk",
                                "ipa",
                                "rar",
                                "zip",
                                "7z",
                                "css",
                                "js",
                                "xml",
                                "ini",
                                "swf",
                                "ico"
                            ],
                            "CacheTime": 86400
                        }
                    ]
                },
                "CacheKey": {
                    "FullUrlCache": "on"
                },
                "Cname": "test.com.com.dsa.dnsv1.com",
                "CreateTime": "2019-12-03 15:23:50",
                "Disable": "normal",
                "Domain": "test.com",
                "ForceRedirect": null,
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
                "Origin": {
                    "Origins": [
                        "1.1.1.1"
                    ],
                    "OriginType": "ip",
                    "ServerName": null,
                    "OriginPullProtocol": "http",
                    "BackupOrigins": [],
                    "BackupOriginType": null
                },
                "ProjectId": 0,
                "Readonly": "normal",
                "ResourceId": "ecdn-xxxxxx",
                "ResponseHeader": {
                    "HeaderRules": [],
                    "Switch": "off"
                },
                "Status": "processing",
                "UpdateTime": "2019-12-03 15:23:50",
                "Tag": [],
                "WebSocket": null
            }
        ],
        "TotalCount": 10
    }
}
```

