**Example 1: 证书关联云资源详情**



Input: 

```
tccli ssl DescribeCertificateBindResourceTaskDetail --cli-unfold-argument  \
    --TaskId 758439 \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "CLB": [
            {
                "Region": "ap-guangzhou",
                "InstanceList": [
                    {
                        "LoadBalancerId": "lb-*****",
                        "LoadBalancerName": "test",
                        "Listeners": [
                            {
                                "ListenerId": "lbl-*****",
                                "ListenerName": "test",
                                "SniSwitch": 1,
                                "Protocol": "https",
                                "Certificate": {
                                    "CertId": "T***jdj",
                                    "DnsNames": [
                                        "www.test.com"
                                    ],
                                    "CertCaId": "T***jdj",
                                    "SSLMode": "mutual"
                                },
                                "Rules": [
                                    {
                                        "LocationId": "/test",
                                        "Domain": "www.test.com",
                                        "IsMatch": true,
                                        "Certificate": {
                                            "CertId": "hr***jdj",
                                            "DnsNames": [
                                                "www.test.com"
                                            ],
                                            "CertCaId": "hr***jdj",
                                            "SSLMode": "mutual"
                                        },
                                        "NoMatchDomains": [
                                            "www.test2.com"
                                        ]
                                    }
                                ],
                                "NoMatchDomains": [
                                    "www.test2.com"
                                ]
                            }
                        ]
                    }
                ],
                "TotalCount": 1,
                "Error": ""
            }
        ],
        "CDN": [
            {
                "TotalCount": 1,
                "InstanceList": [
                    {
                        "Domain": "www.test.com",
                        "CertId": "T***jdj",
                        "Status": "online",
                        "HttpsBillingSwitch": "on"
                    }
                ],
                "Error": ""
            }
        ],
        "WAF": [
            {
                "Region": "ap-guangzhou",
                "InstanceList": [
                    {
                        "Domain": "www.test.com",
                        "CertId": "T***jdj",
                        "Keepalive": 1
                    }
                ],
                "TotalCount": 1,
                "Error": ""
            }
        ],
        "DDOS": [
            {
                "TotalCount": 1,
                "InstanceList": [
                    {
                        "Domain": "www.test.com",
                        "InstanceId": "ddos-*****",
                        "Protocol": "https",
                        "CertId": "T***jdj",
                        "VirtualPort": "443"
                    }
                ],
                "Error": ""
            }
        ],
        "LIVE": [
            {
                "TotalCount": 1,
                "InstanceList": [
                    {
                        "Domain": "www.test.com",
                        "CertId": "T***jdj",
                        "Status": 0
                    }
                ],
                "Error": ""
            }
        ],
        "VOD": [
            {
                "InstanceList": [
                    {
                        "Domain": "www.test.com",
                        "CertId": "T***jdj"
                    }
                ],
                "TotalCount": 1,
                "Error": ""
            }
        ],
        "TKE": [
            {
                "Region": "ap-guangzhou",
                "InstanceList": [
                    {
                        "ClusterId": "test",
                        "ClusterName": "test",
                        "NamespaceList": [
                            {
                                "Name": "test",
                                "SecretList": [
                                    {
                                        "Name": "test",
                                        "CertId": "T***jdj",
                                        "IngressList": [
                                            {
                                                "IngressName": "test",
                                                "TlsDomains": [
                                                    "www.test.com"
                                                ],
                                                "Domains": [
                                                    "www.test.com"
                                                ]
                                            }
                                        ],
                                        "NoMatchDomains": [
                                            "www.test2.com"
                                        ]
                                    }
                                ]
                            }
                        ],
                        "ClusterType": "tke",
                        "ClusterVersion": "1.16"
                    }
                ],
                "TotalCount": 1,
                "Error": ""
            }
        ],
        "APIGATEWAY": [
            {
                "Region": "ap-guangzhou",
                "InstanceList": [
                    {
                        "ServiceId": "service-*****",
                        "ServiceName": "test",
                        "Domain": "www.test.com",
                        "CertId": "T***jdj",
                        "Protocol": "https"
                    }
                ],
                "TotalCount": 1,
                "Error": ""
            }
        ],
        "TCB": [
            {
                "Region": "ap-guangzhou",
                "Error": "",
                "Environments": [
                    {
                        "Environment": {
                            "ID": "TCB-*****",
                            "Source": "cdn",
                            "Name": "test-*****",
                            "Status": "online"
                        },
                        "AccessService": {
                            "InstanceList": [
                                {
                                    "Domain": "www.test.com",
                                    "Status": 0,
                                    "UnionStatus": 0,
                                    "IsPreempted": true,
                                    "ICPStatus": 0,
                                    "OldCertificateId": "jd***jdj"
                                }
                            ],
                            "TotalCount": 0
                        },
                        "HostService": {
                            "InstanceList": [
                                {
                                    "Domain": "www.test.com",
                                    "Status": "online",
                                    "DNSStatus": "online",
                                    "OldCertificateId": "jd***jdj"
                                }
                            ],
                            "TotalCount": 0
                        }
                    }
                ]
            }
        ],
        "TEO": [
            {
                "InstanceList": [
                    {
                        "Host": "www.test.com",
                        "CertId": "T***jdj",
                        "ZoneId": "zone-*****",
                        "Status": "online"
                    }
                ],
                "TotalCount": 1,
                "Error": ""
            }
        ],
        "Status": 1,
        "CacheTime": "2023-10-12 12:00:00",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

