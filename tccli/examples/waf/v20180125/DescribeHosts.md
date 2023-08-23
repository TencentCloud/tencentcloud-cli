**Example 1: 获取防护域名列表**



Input: 

```
tccli waf DescribeHosts --cli-unfold-argument  \
    --Domain www.qcloudwaf.com \
    --DomainId waf-u23yt9Hj \
    --Search aaaa \
    --InstanceID aaaa
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "HostList": [
            {
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
                "Edition": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

