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
            "AddressIPVersion": "abc",
            "IngressName": "abc-xxx",
            "Rules": [
                {
                    "Host": "abc",
                    "Http": {
                        "Paths": [
                            {
                                "Path": "abc",
                                "Backend": {
                                    "ServiceName": "abc",
                                    "ServicePort": 0
                                }
                            }
                        ]
                    },
                    "Protocol": "abc"
                }
            ],
            "ClbId": "lb-xxx",
            "ClusterNamespace": "default",
            "Tls": [
                {
                    "Hosts": [
                        "abc"
                    ],
                    "SecretName": "abc",
                    "CertificateId": "abc"
                }
            ],
            "ClusterId": "abc",
            "Vip": "abc",
            "CreateTime": "abc",
            "Mixed": true,
            "RewriteType": "abc",
            "Domain": "abc"
        },
        "RequestId": "abc-xxx-xxx"
    }
}
```

