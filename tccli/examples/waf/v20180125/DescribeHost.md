**Example 1: 获取防护域名详情**



Input: 

```
tccli waf DescribeHost --cli-unfold-argument  \
    --InstanceID  \
    --Domain  \
    --DomainId 
```

Output: 
```
{
    "Response": {
        "Host": {
            "Domain": "abc",
            "DomainId": "abc",
            "MainDomain": "abc",
            "Mode": 1,
            "Status": 1,
            "State": 1,
            "Engine": 1,
            "IsCdn": 1,
            "LoadBalancerSet": [
                {
                    "LoadBalancerId": "abc",
                    "LoadBalancerName": "abc",
                    "ListenerId": "abc",
                    "ListenerName": "abc",
                    "Vip": "abc",
                    "Vport": 1,
                    "Region": "abc",
                    "Protocol": "abc",
                    "Zone": "abc",
                    "NumericalVpcId": 0,
                    "LoadBalancerType": "abc",
                    "LoadBalancerDomain": "abc"
                }
            ],
            "Region": "abc",
            "Edition": "abc",
            "FlowMode": 1,
            "ClsStatus": 1,
            "Level": 1,
            "CdcClusters": [
                "abc"
            ],
            "AlbType": "abc",
            "IpHeaders": [
                "abc"
            ],
            "EngineType": 0,
            "CloudType": "abc",
            "Note": "abc"
        },
        "RequestId": "abc"
    }
}
```

