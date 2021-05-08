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
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": {
            "ClusterId": "cls-9lxt9ic2",
            "NamespaceId": null,
            "EksNamespace": "default",
            "AddressIPVersion": "IPV4",
            "ClbId": "clb-xxxx",
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
    }
}
```

