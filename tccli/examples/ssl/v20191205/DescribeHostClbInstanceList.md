**Example 1: 查询证书部署CLB实例列表**

查询证书部署CLB实例列表

Input: 

```
tccli ssl DescribeHostClbInstanceList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --CertificateId heh**jej \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --AsyncCache 0 \
    --OldCertificateId hexjx**jj
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "LoadBalancerId": "lb-******",
                "LoadBalancerName": "lb-zrh",
                "Listeners": [
                    {
                        "ListenerId": "lbl-*****",
                        "ListenerName": "lbltest",
                        "SniSwitch": 1,
                        "Protocol": "https",
                        "Certificate": {
                            "CertId": "jejsj**jsj",
                            "DnsNames": [
                                "www.zrh.com"
                            ]
                        },
                        "Rules": [
                            {
                                "LocationId": "lbl-*****",
                                "Domain": "www.zrh.com",
                                "IsMatch": true,
                                "Certificate": {
                                    "CertId": "jesux****",
                                    "DnsNames": [
                                        "www.zrh.com"
                                    ]
                                },
                                "NoMatchDomains": [
                                    "www.zrhtest.com"
                                ]
                            }
                        ],
                        "NoMatchDomains": [
                            "www.zrhtest.com"
                        ]
                    }
                ]
            }
        ],
        "AsyncTotalNum": 0,
        "AsyncOffset": 0,
        "AsyncCacheTime": "2023-12-09 12:00:00",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

