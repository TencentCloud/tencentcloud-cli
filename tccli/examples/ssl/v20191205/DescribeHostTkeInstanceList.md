**Example 1: 获取主机安全服务列表**

获取主机安全服务列表

Input: 

```
tccli ssl DescribeHostTkeInstanceList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --CertificateId abc \
    --IsCache 1 \
    --Filters.0.FilterKey abc \
    --Filters.0.FilterValue abc \
    --AsyncCache 0 \
    --OldCertificateId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "ClusterId": "abc",
                "ClusterName": "abc",
                "NamespaceList": [
                    {
                        "Name": "abc",
                        "SecretList": [
                            {
                                "Name": "abc",
                                "CertId": "abc",
                                "IngressList": [
                                    {
                                        "IngressName": "abc",
                                        "TlsDomains": [
                                            "abc"
                                        ],
                                        "Domains": [
                                            "abc"
                                        ]
                                    }
                                ],
                                "NoMatchDomains": [
                                    "abc"
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "AsyncTotalNum": 0,
        "AsyncOffset": 0,
        "RequestId": "abc"
    }
}
```

