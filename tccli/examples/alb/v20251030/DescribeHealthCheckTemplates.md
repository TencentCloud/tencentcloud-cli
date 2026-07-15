**Example 1: 查询健康检查模板列表**



Input: 

```
tccli alb DescribeHealthCheckTemplates --cli-unfold-argument  \
    --HealthCheckTemplateIds hct-m4x8q2pa \
    --MaxResults 20
```

Output: 
```
{
    "Response": {
        "HealthCheckTemplates": [
            {
                "HealthCheckCodes": [
                    "http_1xx"
                ],
                "HealthCheckHealthyThreshold": 2,
                "HealthCheckHost": "example.com",
                "HealthCheckHttpVersion": "HTTP1.1",
                "HealthCheckInterval": 10,
                "HealthCheckMethod": "GET",
                "HealthCheckPath": "/hello/index.html",
                "HealthCheckPort": 80,
                "HealthCheckProtocol": "HTTP",
                "HealthCheckTemplateId": "hct-m4x8q2pa",
                "HealthCheckTemplateName": "target-group-health-check",
                "CreateTime": "2025-01-01T08:30:00+08:00",
                "ModifyTime": "2025-01-01T08:30:00+08:00",
                "HealthCheckTimeout": 2,
                "HealthCheckUnhealthyThreshold": 2,
                "Tags": [
                    {
                        "TagKey": "key-xxx",
                        "TagValue": "value-xxx"
                    }
                ]
            }
        ],
        "NextToken": "3974ae26e***",
        "TotalCount": 1,
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

