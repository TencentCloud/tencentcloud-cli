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
                "ClusterId": "abc",
                "EnvironmentId": "abc",
                "IngressName": "abc",
                "ClusterNamespace": "default",
                "AddressIPVersion": "IPV4",
                "ClbId": "clb-xxxx",
                "Vip": "abc",
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
                ],
                "CreateTime": "abc",
                "Mixed": true,
                "RewriteType": "abc",
                "Domain": "abc"
            }
        ]
    }
}
```

