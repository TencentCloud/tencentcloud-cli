**Example 1: 查询可绑定证书的域名规则**



Input: 

```
tccli antiddos DescribeL7RulesBySSLCertId --cli-unfold-argument  \
    --Status bindable \
    --CertIds xxx
```

Output: 
```
{
    "Response": {
        "CertSet": [
            {
                "CertId": "kneSCNrZ",
                "L7Rules": [
                    {
                        "InsId": "bgpip-000001eo",
                        "AppId": "251008915",
                        "Protocol": "https",
                        "Domain": "www.xxx.com",
                        "VirtualPort": "443",
                        "SSLId": "",
                        "Status": 8
                    }
                ]
            }
        ],
        "RequestId": "d87b0215-5dc6-4b99-ad82-704f0ef1bfb7"
    }
}
```

