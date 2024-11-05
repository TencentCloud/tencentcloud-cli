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
                "ClusterId": "abc",
                "IngressName": "abc",
                "ClusterNamespace": "default",
                "EnvironmentId": "en-xxxxxx",
                "AddressIPVersion": "IPV4",
                "ClbId": "clb-xxxx",
                "Vip": "abc",
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
                ],
                "CreateTime": "abc",
                "RewriteType": "abc",
                "Domain": "abc"
            }
        ]
    }
}
```

