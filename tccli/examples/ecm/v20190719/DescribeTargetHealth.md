**Example 1: 获取负载均衡后端服务的健康检查状态**



Input: 

```
tccli ecm DescribeTargetHealth --cli-unfold-argument  \
    --LoadBalancerIds lb-f9zyj3kb
```

Output: 
```
{
    "Response": {
        "RequestId": "040f094b-aed7-45fc-963a-ebae4970be44",
        "LoadBalancers": [
            {
                "LoadBalancerId": "lb-f9zyj3kb",
                "LoadBalancerName": "test",
                "Listeners": [
                    {
                        "Rules": [
                            {
                                "Targets": [
                                    {
                                        "HealthStatus": true,
                                        "HealthStatusDetail": "Alive",
                                        "IP": "172.16.0.67",
                                        "Port": 23001,
                                        "TargetId": "ein-ncnepgio"
                                    }
                                ]
                            }
                        ],
                        "ListenerId": "lbl-knd4jr8m",
                        "Port": 13001,
                        "Protocol": "TCP",
                        "ListenerName": ""
                    }
                ]
            }
        ]
    }
}
```

