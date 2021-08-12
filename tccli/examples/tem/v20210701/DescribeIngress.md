**Example 1: 查询 Ingress 规则**

查询 Ingress 规则

Input: 

```
tccli tem DescribeIngress --cli-unfold-argument  \
    --EnvironmentId xx \
    --ClusterNamespace xx \
    --SourceChannel 0 \
    --IngressName xx
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
            "EnvironmentId": "xx",
            "ClusterNamespace": "xx",
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
            "IngressName": "xx",
            "Vip": "xx",
            "Mixed": true,
            "AddressIPVersion": "xx",
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

