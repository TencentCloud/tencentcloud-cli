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
        "DomainRuleSet": [
            {
                "Domain": "abc",
                "RuleSet": [
                    {
                        "RuleId": "abc",
                        "ListenerId": "abc",
                        "Domain": "abc",
                        "Path": "abc",
                        "RealServerType": "abc",
                        "Scheduler": "abc",
                        "HealthCheck": 1,
                        "RuleStatus": 1,
                        "CheckParams": {
                            "DelayLoop": 1,
                            "ConnectTimeout": 1,
                            "Path": "abc",
                            "Method": "abc",
                            "StatusCode": [
                                1
                            ],
                            "Domain": "abc",
                            "FailedCountInter": 1,
                            "FailedThreshold": 1,
                            "BlockInter": 1
                        },
                        "RealServerSet": [
                            {
                                "RealServerId": "abc",
                                "RealServerIP": "abc",
                                "RealServerWeight": 0,
                                "RealServerStatus": 0,
                                "RealServerPort": 0,
                                "DownIPList": [
                                    "abc"
                                ],
                                "RealServerFailoverRole": "abc"
                            }
                        ],
                        "BindStatus": 1,
                        "ForwardHost": "abc",
                        "ServerNameIndicationSwitch": "abc",
                        "ServerNameIndication": "abc",
                        "ForcedRedirect": "abc"
                    }
                ],
                "CertificateId": "abc",
                "CertificateAlias": "abc",
                "ClientCertificateId": "abc",
                "ClientCertificateAlias": "abc",
                "BasicAuthConfId": "abc",
                "BasicAuth": 0,
                "BasicAuthConfAlias": "abc",
                "RealServerCertificateId": "abc",
                "RealServerAuth": 0,
                "RealServerCertificateAlias": "abc",
                "GaapCertificateId": "abc",
                "GaapAuth": 0,
                "GaapCertificateAlias": "abc",
                "RealServerCertificateDomain": "abc",
                "PolyClientCertificateAliasInfo": [
                    {
                        "CertificateId": "abc",
                        "CertificateAlias": "abc"
                    }
                ],
                "PolyRealServerCertificateAliasInfo": [
                    {
                        "CertificateId": "abc",
                        "CertificateAlias": "abc"
                    }
                ],
                "DomainStatus": 1,
                "BanStatus": "abc",
                "Http3Supported": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

