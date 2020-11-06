**Example 1: 获取一个传统型负载均衡的后端服务健康状态信息**



Input: 

```
tccli clb DescribeClassicalLBHealthStatus --cli-unfold-argument  \
    --LoadBalancerId lb-a3u5l5zc
```

Output: 
```
{
    "Response": {
        "HealthList": [
            {
                "IP": "10.142.9.250",
                "Port": 1111,
                "ListenerPort": 111,
                "Protocol": "TCP",
                "HealthStatus": 0
            },
            {
                "IP": "10.104.63.53",
                "Port": 1111,
                "ListenerPort": 111,
                "Protocol": "TCP",
                "HealthStatus": 0
            },
            {
                "IP": "10.104.126.68",
                "Port": 1111,
                "ListenerPort": 111,
                "Protocol": "TCP",
                "HealthStatus": 0
            },
            {
                "IP": "10.142.9.250",
                "Port": 12312,
                "ListenerPort": 1213,
                "Protocol": "UDP",
                "HealthStatus": 1
            },
            {
                "IP": "10.104.126.68",
                "Port": 12312,
                "ListenerPort": 1213,
                "Protocol": "UDP",
                "HealthStatus": 1
            },
            {
                "IP": "10.104.63.53",
                "Port": 12312,
                "ListenerPort": 1213,
                "Protocol": "UDP",
                "HealthStatus": 1
            }
        ],
        "RequestId": "b18d94ba-94fa-4c59-b66c-840d11a6a0f3"
    }
}
```

