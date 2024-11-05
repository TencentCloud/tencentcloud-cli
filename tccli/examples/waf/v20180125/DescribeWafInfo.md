**Example 1: 获取负载均衡绑定的WAF信息**



Input: 

```
tccli waf DescribeWafInfo --cli-unfold-argument  \
    --Params.0.LoadBalancerId lb-14g9fdgm \
    --Params.0.ListenerId lbl-01cby4ig \
    --Params.0.DomainId waf-MyBQKIZe
```

Output: 
```
{
    "Response": {
        "HostList": [
            {
                "LoadBalancer": {
                    "ListenerId": "lbl-01cby4ig",
                    "ListenerName": "test-waf",
                    "LoadBalancerId": "lb-14g9fdgm",
                    "LoadBalancerName": "clbwaftesttest",
                    "Protocol": "HTTP",
                    "Region": "gz",
                    "Vip": "134.171.12.56",
                    "Vport": 80,
                    "Zone": "ap-guangzhou-4",
                    "NumericalVpcId": 546282,
                    "LoadBalancerType": "OPEN",
                    "LoadBalancerDomain": ""
                },
                "Domain": "lsd.qcloudwaf.com",
                "DomainId": "waf-MyBQKIZe",
                "Status": 1,
                "FlowMode": 0
            }
        ],
        "RequestId": "4bcd4d73-f743-466f-a905-205bdd509bec",
        "Total": 1
    }
}
```

