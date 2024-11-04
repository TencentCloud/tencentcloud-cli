**Example 1: 查询转发规则信息**



Input: 

```
tccli gaap DescribeRules --cli-unfold-argument  \
    --ListenerId listener-qjm2tftd
```

Output: 
```
{
    "Response": {
        "RequestId": "83a6736e-5550-4f9e-a2bf-c669e7b3a1d5",
        "TotalCount": 1,
        "DomainRuleSet": [
            {
                "Domain": "baidu.com",
                "IsDefaultServer": false,
                "DomainStatus": 0,
                "Http3Supported": 0,
                "BanStatus": "RECOVER",
                "RuleSet": [],
                "CertificateId": "default",
                "CertificateAlias": "默认证书",
                "ClientCertificateId": "default",
                "ClientCertificateAlias": "默认证书",
                "BasicAuthConfId": null,
                "BasicAuth": 0,
                "BasicAuthConfAlias": null,
                "RealServerCertificateId": null,
                "RealServerAuth": 0,
                "RealServerCertificateAlias": null,
                "RealServerCertificateDomain": null,
                "GaapCertificateId": null,
                "GaapAuth": 0,
                "GaapCertificateAlias": null,
                "PolyClientCertificateAliasInfo": [
                    {
                        "CertificateId": "default",
                        "CertificateAlias": "默认证书"
                    }
                ],
                "PolyRealServerCertificateAliasInfo": [],
                "TLSSupportVersion": [],
                "TLSCiphers": ""
            }
        ]
    }
}
```

