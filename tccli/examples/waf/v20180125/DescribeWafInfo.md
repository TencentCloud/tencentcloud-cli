**Example 1: 获取负载均衡绑定的WAF信息**



Input: 

```
tccli waf DescribeWafInfo --cli-unfold-argument  \
    --Params.0.AppId 251006578 \
    --Params.0.LoadBalancerId lb-A8VF445
```

Output: 
```
{
    "Response": {
        "HostList": [
            {
                "LoadBalancer": {
                    "LoadBalancerId": "A8VF445",
                    "LoadBalancerName": "waftt_test",
                    "ListenerId": "8rI9f73",
                    "ListenerName": "test_listener44_name",
                    "Vip": "203.195.240.4",
                    "Vport": 80,
                    "Region": "gz",
                    "Zone": "广州4区",
                    "Protocol": "http"
                },
                "Domain": "lsd.qcloudwaf.com",
                "DomainId": "waf-MyBQKIZe",
                "Status": 1,
                "FlowMode": 0
            }
        ],
        "RequestId": "4bcd4d73-f743-466f-a905-205bdd509bec"
    }
}
```

