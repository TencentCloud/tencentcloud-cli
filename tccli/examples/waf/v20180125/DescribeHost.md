**Example 1: 获取防护域名详情**



Input: 

```
tccli waf DescribeHost --cli-unfold-argument  \
    --InstanceID xx \
    --Domain xx \
    --DomainId xx
```

Output: 
```
{
    "Response": {
        "Host": {
            "Status": 1,
            "Engine": 1,
            "Domain": "xx",
            "DomainId": "xx",
            "LoadBalancerSet": [
                {
                    "Protocol": "xx",
                    "Zone": "xx",
                    "Region": "xx",
                    "LoadBalancerId": "xx",
                    "ListenerId": "xx",
                    "Vip": "xx",
                    "ListenerName": "xx",
                    "LoadBalancerName": "xx",
                    "Vport": 1
                }
            ],
            "Level": 1,
            "MainDomain": "xx",
            "Region": "xx",
            "FlowMode": 1,
            "State": 1,
            "ClsStatus": 1,
            "IsCdn": 1,
            "Mode": 1,
            "CdcClusters": [
                "xx"
            ],
            "Edition": "xx"
        },
        "RequestId": "xx"
    }
}
```

