**Example 1: 修改健康检查模板**



Input: 

```
tccli alb ModifyHealthCheckTemplate --cli-unfold-argument  \
    --HealthCheckCodes http_1xx \
    --HealthCheckHealthyThreshold 2 \
    --HealthCheckHost example.com \
    --HealthCheckHttpVersion HTTP1.1 \
    --HealthCheckInterval 10 \
    --HealthCheckMethod GET \
    --HealthCheckPath /hello/index.html \
    --HealthCheckPort 80 \
    --HealthCheckProtocol HTTP \
    --HealthCheckTemplateId hct-m4x8q2pa \
    --HealthCheckTemplateName lbtg-0zrnc9qa-template \
    --HealthCheckTimeout 2 \
    --HealthCheckUnhealthyThreshold 2 \
    --Tags.0.TagKey key-xxx \
    --Tags.0.TagValue value-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

