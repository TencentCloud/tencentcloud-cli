**Example 1: 查询 Ingress 规则列表**

查询 Ingress 规则列表

Input: 

```
tccli tem DescribeIngresses --cli-unfold-argument  \
    --ClusterNamespace default \
    --EnvironmentId en-xxxxxx \
    --IngressNames ingress-name \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": [
            {
                "ClusterId": "cls-xxxxxx",
                "EnvironmentId": "en-xxxxxx",
                "IngressName": "ingress-name-xxx",
                "ClusterNamespace": "default",
                "AddressIPVersion": "IPV4",
                "ClbId": "clb-xxxx",
                "Vip": "10.xx.xx.xx",
                "Rules": [
                    {
                        "Host": "",
                        "Http": {
                            "Paths": [
                                {
                                    "Path": "/path",
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
                        "SecretName": "secret-name-xxx"
                    }
                ],
                "CreateTime": "2024-12-04 20:46:29",
                "Mixed": true,
                "RewriteType": "AUTO",
                "Domain": "xxx.xxx.com"
            }
        ]
    }
}
```

