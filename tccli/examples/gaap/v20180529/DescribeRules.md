**Example 1: 查询转发规则信息**



Input: 

```
tccli gaap DescribeRules --cli-unfold-argument  \
    --ListenerId listener-9jt0rtv9
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DomainRuleSet": [
            {
                "GaapCertificateAlias": "gaap-casfdgs",
                "Domain": "www.bbb.com",
                "CertificateId": "cert-mqkdxhcl",
                "RealServerCertificateId": "cert-76es2p6n",
                "CertificateAlias": "test1",
                "BasicAuth": 1,
                "GaapCertificateId": "cert-47teq6gt",
                "RealServerAuth": 1,
                "BasicAuthConfAlias": "basicAuth",
                "BasicAuthConfId": "cert-cqwokbyp",
                "ClientCertificateId": "cert-5n7ifekx",
                "RuleSet": [
                    {
                        "BindStatus": 1,
                        "Domain": "www.bbb.com",
                        "RealServerType": "IP",
                        "RuleId": "rule-hh5xg2yd",
                        "HealthCheck": 0,
                        "ListenerId": "listener-9jt0rtv9",
                        "CheckParams": {
                            "Domain": "www.bbb.com",
                            "ConnectTimeout": 2,
                            "Path": "/",
                            "Method": "HEAD",
                            "DelayLoop": 30,
                            "StatusCode": [
                                100,
                                200,
                                300,
                                400,
                                500
                            ]
                        },
                        "Scheduler": "rr",
                        "Path": "/",
                        "RuleStatus": 0,
                        "RealServerSet": [
                            {
                                "RealServerStatus": 0,
                                "RealServerPort": 234,
                                "RealServerId": "rs-04v3s12c",
                                "DownIPList": [],
                                "RealServerWeight": 1,
                                "RealServerIP": "4.4.4.4"
                            },
                            {
                                "RealServerStatus": 0,
                                "RealServerPort": 424,
                                "RealServerId": "rs-10vtt5en",
                                "DownIPList": [],
                                "RealServerWeight": 1,
                                "RealServerIP": "5.5.5.6"
                            }
                        ]
                    }
                ],
                "GaapAuth": 1,
                "ClientCertificateAlias": "clientCA",
                "RealServerCertificateAlias": "rsca",
                "RealServerCertificateDomain": "www.bbb.com"
            }
        ],
        "RequestId": "6aecde5a-fd9a-4380-8fe9-1e9e4a98b7b5"
    }
}
```

