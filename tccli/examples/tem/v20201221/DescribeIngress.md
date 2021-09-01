**Example 1: 查询 Ingress 规则**

查询 Ingress 规则

Input: 

```
tccli tem DescribeIngress --cli-unfold-argument  \
    --NamespaceId env-xxx \
    --EksNamespace default \
    --Name xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Tls": [
                {
                    "CertificateId": "xx",
                    "Hosts": [
                        "xxx.com"
                    ],
                    "SecretName": "xx"
                }
            ],
            "EksNamespace": "xx",
            "Name": "xx",
            "Rules": [
                {
                    "Protocol": "xx",
                    "Host": "xx",
                    "Http": {
                        "Paths": [
                            {
                                "Path": "xx",
                                "Backend": {
                                    "ServiceName": "xx",
                                    "ServicePort": 443
                                }
                            }
                        ]
                    }
                }
            ],
            "ClbId": "xx",
            "ClusterId": "xx",
            "CreateTime": "xx",
            "Vip": "xx",
            "Mixed": true,
            "AddressIPVersion": "xx",
            "NamespaceId": "xx"
        },
        "RequestId": "xx"
    }
}
```

