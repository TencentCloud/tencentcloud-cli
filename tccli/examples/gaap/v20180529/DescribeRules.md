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
                "GaapCertificateAlias": "xx",
                "Domain": "xx",
                "CertificateId": "xx",
                "PolyRealServerCertificateAliasInfo": [
                    {
                        "CertificateId": "xx",
                        "CertificateAlias": "xx"
                    }
                ],
                "RealServerCertificateId": "xx",
                "BanStatus": "BANNED",
                "CertificateAlias": "xx",
                "ClientCertificateId": "xx",
                "GaapCertificateId": "xx",
                "BasicAuth": 1,
                "BasicAuthConfAlias": "xx",
                "BasicAuthConfId": "xx",
                "RealServerCertificateAlias": "xx",
                "RuleSet": [
                    {
                        "BindStatus": 1,
                        "Domain": "xx",
                        "RealServerType": "xx",
                        "ForwardHost": "xx",
                        "RuleId": "xx",
                        "HealthCheck": 1,
                        "ListenerId": "xx",
                        "CheckParams": {
                            "Domain": "xx",
                            "ConnectTimeout": 1,
                            "BlockInter": 1,
                            "FailedThreshold": 1,
                            "Path": "xx",
                            "FailedCountInter": 1,
                            "Method": "xx",
                            "DelayLoop": 1,
                            "StatusCode": [
                                1,
                                1,
                                1,
                                1,
                                1
                            ]
                        },
                        "Scheduler": "xx",
                        "Path": "xx",
                        "RuleStatus": 1,
                        "RealServerSet": [
                            {
                                "RealServerStatus": 0,
                                "RealServerPort": 234,
                                "RealServerId": "xx",
                                "DownIPList": [
                                    "xx"
                                ],
                                "RealServerWeight": 1,
                                "RealServerIP": "xx"
                            },
                            {
                                "RealServerStatus": 0,
                                "RealServerPort": 424,
                                "RealServerId": "xx",
                                "RealServerWeight": 1,
                                "DownIPList": [
                                    "xx"
                                ],
                                "RealServerIP": "xx"
                            }
                        ]
                    }
                ],
                "PolyClientCertificateAliasInfo": [
                    {
                        "CertificateId": "xx",
                        "CertificateAlias": "xx"
                    }
                ],
                "GaapAuth": 1,
                "ClientCertificateAlias": "xx",
                "RealServerAuth": 1,
                "RealServerCertificateDomain": "xx",
                "DomainStatus": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

