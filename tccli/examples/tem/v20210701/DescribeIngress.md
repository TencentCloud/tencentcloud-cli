**Example 1: 查询 Ingress 规则**

查询 Ingress 规则

Input: 

```
tccli tem DescribeIngress --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ClusterNamespace default \
    --SourceChannel 0 \
    --IngressName name-xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "EnvironmentId": "en-xxxxxx",
            "AddressIPVersion": "IPV4",
            "IngressName": "ingress-name-xxx",
            "Rules": [
                {
                    "Host": "11.xx.xx.xx",
                    "Http": {
                        "Paths": [
                            {
                                "Path": "/path",
                                "Backend": {
                                    "ServiceName": "svc-name-xxx",
                                    "ServicePort": 8080
                                }
                            }
                        ]
                    },
                    "Protocol": "TCP"
                }
            ],
            "ClbId": "lb-xxx",
            "ClusterNamespace": "default",
            "Tls": [
                {
                    "Hosts": [
                        "11.xx.xx.xx"
                    ],
                    "SecretName": "secret-name-xxx",
                    "CertificateId": "certId-xxx"
                }
            ],
            "ClusterId": "cls-xxxxxx",
            "Vip": "11.xx.xx.xx",
            "CreateTime": "2024-12-04 20:46:29",
            "Mixed": true,
            "RewriteType": "AUTO",
            "Domain": ""
        },
        "RequestId": "abc-xxx-xxx-xxx"
    }
}
```

