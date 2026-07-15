**Example 1: 查询 EnvironmentTemplate 列表**



Input: 

```
tccli ags DescribeEnvironmentTemplateList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name environment-template-name \
    --Filters.0.Values example-environment-template
```

Output: 
```
{
    "Response": {
        "EnvironmentTemplateSet": [
            {
                "EnvironmentTemplateId": "envt-example",
                "EnvironmentTemplateName": "example-environment-template",
                "EnvironmentTemplateConfig": {
                    "Image": "example.com/agent-engine/example-environment:v1",
                    "Command": [
                        "/usr/local/bin/example-environment"
                    ],
                    "Args": [
                        "serve",
                        "--listen",
                        ":8080"
                    ],
                    "Env": [
                        {
                            "Name": "EXAMPLE_ENVIRONMENT_MODE",
                            "Value": "demo"
                        }
                    ],
                    "Resources": {
                        "CPU": "1000m",
                        "Memory": "512Mi"
                    },
                    "Ports": [
                        {
                            "Name": "http",
                            "Port": 8080,
                            "Protocol": "TCP"
                        }
                    ],
                    "HealthCheck": {
                        "HttpGet": {
                            "Path": "/healthz",
                            "Port": 8080,
                            "Scheme": "HTTP"
                        }
                    }
                },
                "ProviderConfig": {
                    "ProviderKind": "TENCENT_AGS",
                    "TencentAGS": {
                        "RoleArn": "qcs::cam::uin/123456789012:roleName/example-environment-role",
                        "ImageRegistryType": "personal",
                        "NetworkConfiguration": {
                            "NetworkMode": "PUBLIC"
                        }
                    }
                },
                "ProviderStatus": {
                    "TencentAGS": {
                        "ToolId": "sdt-example-environment"
                    }
                },
                "Status": "ACTIVE",
                "CreatedTime": "2026-07-03T10:56:18Z",
                "UpdatedTime": "2026-07-03T10:56:18Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

