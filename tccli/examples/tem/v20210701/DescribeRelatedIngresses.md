**Example 1: 查询应用关联的 Ingress 规则列表**

查询应用关联的 Ingress 规则列表

Input: 

```
tccli tem DescribeRelatedIngresses --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ClusterNamespace default \
    --ApplicationId app-xxxxxx \
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
                "IngressName": "ingress-name-xxx",
                "ClusterNamespace": "default",
                "EnvironmentId": "en-xxxxxx",
                "AddressIPVersion": "IPV4",
                "ClbId": "clb-xxxx",
                "Vip": "10.xx.xx.xx",
                "Mixed": true,
                "Rules": [
                    {
                        "Host": "",
                        "Http": {
                            "Paths": [
                                {
                                    "Path": "/path",
                                    "Backend": {
                                        "ServiceName": "svc-name-xxx",
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
                "RewriteType": "AUTO",
                "Domain": "xxx.xxx.com"
            }
        ]
    }
}
```

