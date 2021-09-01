**Example 1: Ingress 列表**

Ingress 列表

Input: 

```
tccli tem DescribeIngresses --cli-unfold-argument  \
    --NamespaceId env-xxx \
    --EksNamespace default \
    --Names test-ingress-1
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

