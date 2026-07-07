**Example 1: 创建健康检查模板**



Input: 

```
tccli alb CreateHealthCheckTemplate --cli-unfold-argument  \
    --HealthCheckCodes http_1xx \
    --HealthCheckHealthyThreshold 2 \
    --HealthCheckHost example.com \
    --HealthCheckHttpVersion HTTP1.1 \
    --HealthCheckInterval 10 \
    --HealthCheckMethod GET \
    --HealthCheckPath /hello/index.html \
    --HealthCheckPort 80 \
    --HealthCheckProtocol HTTP \
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
        "HealthCheckTemplateId": "hct-m4x8q2pa",
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

