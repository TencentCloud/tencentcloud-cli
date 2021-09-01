**Example 1: 获取黑石负载均衡端口相关信息**



Input: 

```
tccli bmlb DescribeLoadBalancerPortInfo --cli-unfold-argument  \
    --LoadBalancerId lb-q7qoi8cr
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "ListenerId": "lbl-4n8mp2dj",
                "ListenerName": "test",
                "LoadBalancerPort": 80,
                "Port": 0,
                "Protocol": "http",
                "Bandwidth": 0,
                "Status": 1
            },
            {
                "ListenerId": "lbl-rax7qrr7",
                "ListenerName": "8000",
                "LoadBalancerPort": 8000,
                "Port": 0,
                "Protocol": "tcp",
                "Bandwidth": 0,
                "Status": 1
            }
        ],
        "RequestId": "546ca47f-c1f0-41a6-8783-11ad13734dea"
    }
}
```

