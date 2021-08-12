**Example 1: 查询 Ingress 规则列表**

查询 Ingress 规则列表

Input: 

```
tccli tem DescribeIngresses --cli-unfold-argument  \
    --ClusterNamespace xx \
    --EnvironmentId xx \
    --IngressNames xx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": [
            {
                "ClusterId": "cls-9lxt9ic2",
                "AddressIPVersion": "IPV4",
                "ClbId": "clb-xxxx",
                "Vip": "10.10.10.10",
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

