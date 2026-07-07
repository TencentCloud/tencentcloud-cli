**Example 1: 修改目标组**



Input: 

```
tccli alb ModifyTargetGroupAttributes --cli-unfold-argument  \
    --HealthCheckConfig.HealthCheckCodes http_1xx \
    --HealthCheckConfig.HealthCheckEnabled True \
    --HealthCheckConfig.HealthCheckHealthyThreshold 2 \
    --HealthCheckConfig.HealthCheckHost example.com \
    --HealthCheckConfig.HealthCheckHttpVersion HTTP1.1 \
    --HealthCheckConfig.HealthCheckInterval 10 \
    --HealthCheckConfig.HealthCheckMethod GET \
    --HealthCheckConfig.HealthCheckPath /hello/index.html \
    --HealthCheckConfig.HealthCheckPort 80 \
    --HealthCheckConfig.HealthCheckProtocol HTTP \
    --HealthCheckConfig.HealthCheckTimeout 2 \
    --HealthCheckConfig.HealthCheckUnhealthyThreshold 2 \
    --KeepaliveEnabled True \
    --SchedulerAlgorithm wrr \
    --StickySessionConfig.Cookie SERVERID \
    --StickySessionConfig.CookieTimeout 20 \
    --StickySessionConfig.StickySessionEnabled True \
    --StickySessionConfig.StickySessionType Insert \
    --TargetGroupId lbtg-0zrnc9qa \
    --TargetGroupName test-group
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

