**Example 1: demo**



Input: 

```
tccli tse UpdateUpstreamHealthCheckConfig --cli-unfold-argument  \
    --GatewayId abc \
    --Name abc \
    --HealthCheckConfig.EnableActiveHealthCheck True \
    --HealthCheckConfig.ActiveHealthCheck.HealthyInterval 1 \
    --HealthCheckConfig.ActiveHealthCheck.UnHealthyInterval 1 \
    --HealthCheckConfig.ActiveHealthCheck.HttpPath abc \
    --HealthCheckConfig.EnablePassiveHealthCheck True \
    --HealthCheckConfig.PassiveHealthCheck.Type abc \
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
        "RequestId": "abc"
    }
}
```

