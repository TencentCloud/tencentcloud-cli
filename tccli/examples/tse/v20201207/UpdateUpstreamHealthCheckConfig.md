**Example 1: 更新云原生网关健康检查配置**



Input: 

```
tccli tse UpdateUpstreamHealthCheckConfig --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Name 公网入口 \
    --HealthCheckConfig.EnableActiveHealthCheck True \
    --HealthCheckConfig.ActiveHealthCheck.HealthyInterval 1 \
    --HealthCheckConfig.ActiveHealthCheck.UnHealthyInterval 1 \
    --HealthCheckConfig.ActiveHealthCheck.HttpPath /v1/users \
    --HealthCheckConfig.EnablePassiveHealthCheck True \
    --HealthCheckConfig.PassiveHealthCheck.Type http \
    --HealthCheckConfig.Successes 1 \
    --HealthCheckConfig.Failures 1 \
    --HealthCheckConfig.Timeouts 1 \
    --HealthCheckConfig.HealthyHttpStatuses 1 \
    --HealthCheckConfig.UnhealthyHttpStatuses 1
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

