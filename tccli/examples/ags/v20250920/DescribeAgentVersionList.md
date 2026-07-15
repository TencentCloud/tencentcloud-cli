**Example 1: 查询 AgentVersion 列表**



Input: 

```
tccli ags DescribeAgentVersionList --cli-unfold-argument  \
    --AgentId ag-example \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name version \
    --Filters.0.Values v2
```

Output: 
```
{
    "Response": {
        "AgentVersionSet": [
            {
                "AgentId": "ag-example",
                "Version": "v2",
                "AgentConfig": {
                    "Image": "example.com/agent-engine/example-agent:v2",
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
                        "ToolId": "sdt-example-agent-v1"
                    }
                },
                "DefaultWorkspaceTemplateId": "wst-example",
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

