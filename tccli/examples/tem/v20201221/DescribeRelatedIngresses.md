**Example 1: 服务关联的 Ingress 列表**

服务关联的 Ingress 列表

Input: 

```
tccli tem DescribeRelatedIngresses --cli-unfold-argument  \
    --NamespaceId env-xxx \
    --EksNamespace default \
    --ServiceId svc-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": [
            {
                "ClusterId": "cls-9lxt9ic2",
                "NamespaceId": null,
                "EksNamespace": "default",
                "AddressIPVersion": "IPV4",
                "ClbId": "clb-xxxx",
                "Vip": "10.10.10.10",
                "Name": "test-ingress-1",
                "Mixed": true,
                "Rules": [
                    {
                        "Host": "",
                        "Http": {
                            "Paths": [
                                {
                                    "Path": "/",
                                    "Backend": {
                                        "ServiceName": "kubernetes",
                                        "ServicePort": 443
                                    }
                                }
                            ]
                        }
                    }
                ],
                "Tls": [
                    {
                        "Hosts": [
                            "xxx.com"
                        ],
                        "SecretName": "xxx"
                    }
                ]
            }
        ]
    }
}
```

