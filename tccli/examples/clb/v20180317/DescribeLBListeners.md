**Example 1: 查询云主机绑定的负载均衡**



Input: 

```
tccli clb DescribeLBListeners --cli-unfold-argument  \
    --Backends.0.VpcId vpc-xxxxx \
    --Backends.0.PrivateIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "LoadBalancers": [
            {
                "LoadBalancerId": "lb-xxxxx",
                "Vip": "10.0.0.1",
                "Region": "ap-guangzhou",
                "Listeners": [
                    {
                        "ListenerId": "lbl-xxxxx",
                        "Protocol": "TCP",
                        "Port": 81,
                        "EndPort": 0,
                        "Rules": null,
                        "Targets": [
                            {
                                "Type": "eni",
                                "PrivateIp": "10.0.0.2",
                                "Port": 1201,
                                "VpcId": 1111,
                                "Weight": 10
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba22"
    }
}
```

