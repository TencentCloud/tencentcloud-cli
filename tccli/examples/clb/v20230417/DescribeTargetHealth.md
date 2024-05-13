**Example 1: 查询负载均衡实例的后端健康状态**

查询负载均衡实例的后端健康状态

Input: 

```
tccli clb DescribeTargetHealth --cli-unfold-argument  \
    --LoadBalancerIds lb-qc2iq5yc
```

Output: 
```
{
    "Response": {
        "LoadBalancers": [
            {
                "LoadBalancerId": "lb-xxxxxxxx",
                "LoadBalancerName": "xxxxx",
                "Listeners": [
                    {
                        "ListenerId": "lbl-xxxxxxxx",
                        "ListenerName": "80",
                        "Protocol": "HTTP",
                        "Port": 80,
                        "Rules": [
                            {
                                "LocationId": "loc-xxxxxxxx",
                                "Domain": "kq.xxxxxx.com.cn",
                                "Url": "/",
                                "Targets": [
                                    {
                                        "TargetId": "cvm-xxxxxxxx",
                                        "IP": "x.x.x.x",
                                        "Port": 80,
                                        "HealthStatus": true,
                                        "HealthStatusDetail": "Alive"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "e3a60a20-d994-48d6-b971-3bd05aa1aae6"
    }
}
```

