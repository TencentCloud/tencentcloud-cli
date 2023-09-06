**Example 1: 证书关联云资源详情**



Input: 

```
tccli ssl DescribeCertificateBindResourceTaskDetail --cli-unfold-argument  \
    --TaskId abc \
    --Limit abc \
    --Offset abc
```

Output: 
```
{
    "Response": {
        "CLB": [
            {
                "Region": "abc",
                "InstanceList": [
                    {
                        "LoadBalancerId": "abc",
                        "LoadBalancerName": "abc",
                        "Listeners": [
                            {
                                "ListenerId": "abc",
                                "ListenerName": "abc",
                                "SniSwitch": 1,
                                "Protocol": "abc",
                                "Certificate": {
                                    "CertId": "abc",
                                    "DnsNames": [
                                        "abc"
                                    ],
                                    "CertCaId": "abc",
                                    "SSLMode": "abc"
                                },
                                "Rules": [
                                    {
                                        "LocationId": "abc",
                                        "Domain": "abc",
                                        "IsMatch": true,
                                        "Certificate": {
                                            "CertId": "abc",
                                            "DnsNames": [
                                                "abc"
                                            ],
                                            "CertCaId": "abc",
                                            "SSLMode": "abc"
                                        },
                                        "NoMatchDomains": [
                                            "abc"
                                        ]
                                    }
                                ],
                                "NoMatchDomains": [
                                    "abc"
                                ]
                            }
                        ]
                    }
                ],
                "TotalCount": 1
            }
        ],
        "CDN": [
            {
                "TotalCount": 1,
                "InstanceList": [
                    {
                        "Domain": "abc",
                        "CertId": "abc",
                        "Status": "abc",
                        "HttpsBillingSwitch": "abc"
                    }
                ]
            }
        ],
        "WAF": [
            {
                "Region": "abc",
                "InstanceList": [
                    {
                        "Domain": "abc",
                        "CertId": "abc",
                        "Keepalive": 1
                    }
                ],
                "TotalCount": 1
            }
        ],
        "DDOS": [
            {
                "TotalCount": 1,
                "InstanceList": [
                    {
                        "Domain": "abc",
                        "InstanceId": "abc",
                        "Protocol": "abc",
                        "CertId": "abc",
                        "VirtualPort": "abc"
                    }
                ]
            }
        ],
        "LIVE": [
            {
                "TotalCount": 1,
                "InstanceList": [
                    {
                        "Domain": "abc",
                        "CertId": "abc",
                        "Status": 0
                    }
                ]
            }
        ],
        "VOD": [
            {
                "InstanceList": [
                    {
                        "Domain": "abc",
                        "CertId": "abc"
                    }
                ],
                "TotalCount": 1
            }
        ],
        "TKE": [
            {
                "Region": "abc",
                "InstanceList": [
                    {
                        "ClusterId": "abc",
                        "ClusterName": "abc",
                        "NamespaceList": [
                            {
                                "Name": "abc",
                                "SecretList": [
                                    {
                                        "Name": "abc",
                                        "CertId": "abc",
                                        "IngressList": [
                                            {
                                                "IngressName": "abc",
                                                "TlsDomains": [
                                                    "abc"
                                                ],
                                                "Domains": [
                                                    "abc"
                                                ]
                                            }
                                        ],
                                        "NoMatchDomains": [
                                            "abc"
                                        ]
                                    }
                                ]
                            }
                        ],
                        "ClusterType": "abc",
                        "ClusterVersion": "abc"
                    }
                ],
                "TotalCount": 1
            }
        ],
        "APIGATEWAY": [
            {
                "Region": "abc",
                "InstanceList": [
                    {
                        "ServiceId": "abc",
                        "ServiceName": "abc",
                        "Domain": "abc",
                        "CertId": "abc",
                        "Protocol": "abc"
                    }
                ],
                "TotalCount": 1
            }
        ],
        "TCB": [
            {
                "Region": "abc",
                "Environments": [
                    {
                        "Environment": {
                            "ID": "abc",
                            "Source": "abc",
                            "Name": "abc",
                            "Status": "abc"
                        },
                        "AccessService": {
                            "InstanceList": [
                                {
                                    "Domain": "abc",
                                    "Status": 0,
                                    "UnionStatus": 0,
                                    "IsPreempted": true,
                                    "ICPStatus": 0,
                                    "OldCertificateId": "abc"
                                }
                            ],
                            "TotalCount": 0
                        },
                        "HostService": {
                            "InstanceList": [
                                {
                                    "Domain": "abc",
                                    "Status": "abc",
                                    "DNSStatus": "abc",
                                    "OldCertificateId": "abc"
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
                        "Host": "abc",
                        "CertId": "abc",
                        "ZoneId": "abc",
                        "Status": "abc"
                    }
                ],
                "TotalCount": 1
            }
        ],
        "Status": 1,
        "CacheTime": "abc",
        "RequestId": "abc"
    }
}
```

