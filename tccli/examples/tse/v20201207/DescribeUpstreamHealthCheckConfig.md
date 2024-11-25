**Example 1: 获取云原生网关服务健康检查配置**



Input: 

```
tccli tse DescribeUpstreamHealthCheckConfig --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Name 公网入口服务
```

Output: 
```
{
    "Response": {
        "Result": {
            "EnableActiveHealthCheck": true,
            "ActiveHealthCheck": {
                "HealthyInterval": 1,
                "UnHealthyInterval": 1,
                "HttpPath": "/health"
            },
            "EnablePassiveHealthCheck": true,
            "PassiveHealthCheck": {
                "Type": "/health"
            },
            "Successes": 1,
            "Failures": 1,
            "Timeouts": 1,
            "HealthyHttpStatuses": [
                1
            ],
            "UnhealthyHttpStatuses": [
                1
            ]
        },
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

