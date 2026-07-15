**Example 1: 创建 EnvironmentTemplate**



Input: 

```
tccli ags CreateEnvironmentTemplate --cli-unfold-argument  \
    --EnvironmentTemplateName example-environment-template \
    --EnvironmentTemplateConfig.Image example.com/agent-engine/example-environment:v1 \
    --EnvironmentTemplateConfig.Command /usr/local/bin/example-environment \
    --EnvironmentTemplateConfig.Args serve --listen :8080 \
    --EnvironmentTemplateConfig.Env.0.Name EXAMPLE_ENVIRONMENT_MODE \
    --EnvironmentTemplateConfig.Env.0.Value demo \
    --EnvironmentTemplateConfig.Resources.CPU 1000m \
    --EnvironmentTemplateConfig.Resources.Memory 512Mi \
    --EnvironmentTemplateConfig.Ports.0.Name http \
    --EnvironmentTemplateConfig.Ports.0.Port 8080 \
    --EnvironmentTemplateConfig.Ports.0.Protocol TCP \
    --EnvironmentTemplateConfig.HealthCheck.HttpGet.Path /healthz \
    --EnvironmentTemplateConfig.HealthCheck.HttpGet.Port 8080 \
    --EnvironmentTemplateConfig.HealthCheck.HttpGet.Scheme HTTP \
    --ProviderConfig.ProviderKind TENCENT_AGS \
    --ProviderConfig.TencentAGS.RoleArn qcs::cam::uin/123456789012:roleName/example-environment-role \
    --ProviderConfig.TencentAGS.ImageRegistryType personal \
    --ProviderConfig.TencentAGS.NetworkConfiguration.NetworkMode PUBLIC
```

Output: 
```
{
    "Response": {
        "EnvironmentTemplate": {
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
                    "ToolId": ""
                }
            },
            "Status": "CREATING",
            "CreatedTime": "2026-07-03T10:56:18Z",
            "UpdatedTime": "2026-07-03T10:56:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

