**Example 1: 查询证书绑定的云资源**



Input: 

```
tccli ssl DescribeCertificateBindResourceTaskDetail --cli-unfold-argument  \
    --TaskId 37710177
```

Output: 
```
{
    "Response": {
        "APIGATEWAY": [
            {
                "Error": "",
                "InstanceList": [],
                "Region": "ap-guangzhou",
                "TotalCount": 0
            }
        ],
        "CDN": [
            {
                "Error": "",
                "InstanceList": [],
                "TotalCount": 0
            }
        ],
        "CLB": [
            {
                "Error": "",
                "InstanceList": [],
                "Region": "ap-guangzhou",
                "TotalCount": 0
            }
        ],
        "COS": [
            {
                "Error": "",
                "InstanceList": [],
                "Region": "ap-nanjing",
                "TotalCount": 0
            }
        ],
        "CacheTime": "2025-12-12 15:42:46",
        "DDOS": [
            {
                "Error": "",
                "InstanceList": [],
                "TotalCount": 0
            }
        ],
        "GAAP": [
            {
                "Error": "",
                "InstanceList": [
                    {
                        "InstanceId": "ga-9ri8fhos",
                        "InstanceName": "ssltest",
                        "ListenerList": [
                            {
                                "CertIdList": [
                                    "TVPV0B8A"
                                ],
                                "ListenerId": "lsr-g1f9fth1",
                                "ListenerName": "ssl",
                                "ListenerStatus": "ACTIVE",
                                "NoMatchDomains": [
                                    "xinge-test-2020112002.cn"
                                ],
                                "Protocol": "HTTPS"
                            }
                        ]
                    }
                ],
                "TotalCount": 1
            }
        ],
        "LIVE": [
            {
                "Error": "",
                "InstanceList": [],
                "TotalCount": 0
            }
        ],
        "MQTT": [
            {
                "Error": "",
                "InstanceList": [
                    {
                        "CaCertIdList": [
                            "QmRR1PkY"
                        ],
                        "InstanceId": "mqtt-9xgzvm2g",
                        "InstanceName": "ssl",
                        "InstanceStatus": "RUNNING",
                        "NoMatchDomains": [
                            "xinge-test-2020112002.cn"
                        ],
                        "ServerCertIdList": [
                            "N6MDRovP"
                        ]
                    }
                ],
                "Region": "ap-guangzhou",
                "TotalCount": 1
            }
        ],
        "SCF": [
            {
                "Error": "",
                "InstanceList": [
                    {
                        "CertificateId": "TVPV0B8A",
                        "Domain": "xinge-test-2020112002.cn",
                        "Protocol": "HTTP&HTTPS",
                        "Region": "ap-guangzhou"
                    }
                ],
                "Region": "ap-guangzhou",
                "TotalCount": 1
            }
        ],
        "Status": 1,
        "TCB": [
            {
                "Environments": [
                    {
                        "AccessService": {
                            "InstanceList": [],
                            "TotalCount": 0
                        },
                        "Environment": {
                            "ID": "dns-ssl-8gdfg2h1ff43c5ab",
                            "Name": "dns-ssl",
                            "Source": "qcloud",
                            "Status": "NORMAL"
                        },
                        "HostService": {
                            "InstanceList": [],
                            "TotalCount": 0
                        }
                    }
                ],
                "Error": "",
                "Region": "ap-guangzhou"
            }
        ],
        "TDMQ": [
            {
                "Error": "",
                "InstanceList": [
                    {
                        "CaCertId": "RDU0LL2y",
                        "CertId": "TVPV0B8A",
                        "InstanceId": "amqp-7dx2ozor",
                        "InstanceName": "ssl",
                        "InstanceStatus": "HEALTHY",
                        "NoMatchDomains": [
                            "xinge-test-2020112002.cn"
                        ]
                    }
                ],
                "Region": "ap-guangzhou",
                "TotalCount": 1
            }
        ],
        "TEO": [
            {
                "Error": "",
                "InstanceList": [],
                "TotalCount": 0
            }
        ],
        "TKE": [
            {
                "Error": "",
                "InstanceList": [],
                "Region": "ap-guangzhou-lwy-cft",
                "TotalCount": 0
            }
        ],
        "TSE": [
            {
                "Error": "",
                "InstanceList": [],
                "Region": "ap-guangzhou",
                "TotalCount": 0
            }
        ],
        "VOD": [
            {
                "Error": "",
                "InstanceList": [],
                "TotalCount": 0
            }
        ],
        "WAF": [
            {
                "Error": "",
                "InstanceList": [],
                "Region": "ap-guangzhou",
                "TotalCount": 0
            }
        ],
        "RequestId": "c1fc42bb-93b5-405b-81a8-75625bd56195"
    }
}
```

