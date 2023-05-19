**Example 1: 获取主机安全服务列表**

获取主机安全服务列表

Input: 

```
tccli ssl DescribeHostClbInstanceList --cli-unfold-argument  \
    --IsCache 1 \
    --CertificateId xx \
    --Limit 1 \
    --Filters.0.FilterKey xx \
    --Filters.0.FilterValue xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "Listeners": [
                    {
                        "Protocol": "xx",
                        "Certificate": {
                            "CertId": "xx",
                            "DnsNames": [
                                "xx"
                            ]
                        },
                        "Rules": [
                            {
                                "IsMatch": true,
                                "Domain": "xx",
                                "LocationId": "xx",
                                "Certificate": {
                                    "CertId": "xx",
                                    "DnsNames": [
                                        "xx"
                                    ]
                                }
                            }
                        ],
                        "SniSwitch": 1,
                        "ListenerId": "xx",
                        "ListenerName": "xx"
                    }
                ],
                "LoadBalancerName": "xx",
                "LoadBalancerId": "xx"
            }
        ],
        "RequestId": "xx",
        "AsyncOffset": 0,
        "AsyncTotalNum": 0
    }
}
```

