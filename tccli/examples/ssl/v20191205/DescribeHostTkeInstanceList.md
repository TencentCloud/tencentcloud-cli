**Example 1: 证书部署TKE实例列表**

证书部署TKE实例列表

Input: 

```
tccli ssl DescribeHostTkeInstanceList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --CertificateId tke-****** \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --AsyncCache 0 \
    --OldCertificateId J**kk
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "ClusterId": "tke-******",
                "ClusterName": "tke****",
                "ClusterType": "n**w",
                "ClusterVersion": "3.8.***.1",
                "NamespaceList": [
                    {
                        "Name": "zrh",
                        "SecretList": [
                            {
                                "Name": "zrh",
                                "CertId": "jj**kk",
                                "IngressList": [
                                    {
                                        "IngressName": "zrh",
                                        "TlsDomains": [
                                            "www.zrh,com"
                                        ],
                                        "Domains": [
                                            "ww.zrh.com"
                                        ]
                                    }
                                ],
                                "NoMatchDomains": [
                                    "www.zyh.com"
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "AsyncTotalNum": 0,
        "AsyncOffset": 0,
        "AsyncCacheTime": "10",
        "RequestId": "c9c9d2fb-41c0-43b6-8c10-44c81de553c1"
    }
}
```

