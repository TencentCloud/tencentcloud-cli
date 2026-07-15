**Example 1: 创建 Agent 资源**



Input: 

```
tccli ags CreateAgent --cli-unfold-argument  \
    --AgentName example-agent \
    --AgentType CLOUD \
    --InitialVersion v1 \
    --AgentConfig.Image example.com/agent-engine/example-agent:v1 \
    --AgentConfig.Command /usr/local/bin/example-agent \
    --AgentConfig.Args serve --port 8080 \
    --AgentConfig.Env.0.Name EXAMPLE_LOG_LEVEL \
    --AgentConfig.Env.0.Value info \
    --AgentConfig.Resources.CPU 1000m \
    --AgentConfig.Resources.Memory 512Mi \
    --AgentConfig.Ports.0.Name http \
    --AgentConfig.Ports.0.Port 8080 \
    --AgentConfig.Ports.0.Protocol TCP \
    --AgentConfig.HealthCheck.HttpGet.Path /healthz \
    --AgentConfig.HealthCheck.HttpGet.Port 8080 \
    --AgentConfig.HealthCheck.HttpGet.Scheme HTTP \
    --ProviderConfig.ProviderKind TENCENT_AGS \
    --ProviderConfig.TencentAGS.RoleArn qcs::cam::uin/123456789012:roleName/example-agent-engine-role \
    --ProviderConfig.TencentAGS.ImageRegistryType personal \
    --ProviderConfig.TencentAGS.NetworkConfiguration.NetworkMode PUBLIC \
    --DefaultWorkspaceTemplateId wst-example
```

Output: 
```
{
    "Response": {
        "Agent": {
            "AgentId": "ag-example",
            "AgentName": "example-agent",
            "AgentType": "CLOUD",
            "DefaultVersion": "v1",
            "Status": "CREATING",
            "CreatedTime": "2026-07-03T10:56:18Z",
            "UpdatedTime": "2026-07-03T10:56:18Z"
        },
        "AgentVersion": {
            "AgentId": "ag-example",
            "Version": "v1",
            "AgentConfig": {
                "Image": "example.com/agent-engine/example-agent:v1",
                "Command": [
                    "/usr/local/bin/example-agent"
                ],
                "Args": [
                    "serve",
                    "--port",
                    "8080"
                ],
                "Env": [
                    {
                        "Name": "EXAMPLE_LOG_LEVEL",
                        "Value": "info"
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
                    "RoleArn": "qcs::cam::uin/123456789012:roleName/example-agent-engine-role",
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
            "DefaultWorkspaceTemplateId": "wst-example",
            "Status": "CREATING",
            "CreatedTime": "2026-07-03T10:56:18Z",
            "UpdatedTime": "2026-07-03T10:56:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

