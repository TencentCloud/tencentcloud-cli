**Example 1: 创建成功**



Input: 

```
tccli ags CreateAgentVersion --cli-unfold-argument  \
    --AgentId ag-0c6c69201e87d43229f82b485d69311b \
    --AgentVersion v2 \
    --AgentConfig.Image ccr.ccs.tencentyun.com/ags.dev/nginx:alpine \
    --AgentConfig.Command nginx \
    --AgentConfig.Args -g \
    --AgentConfig.Env.0.Name TEST_ENV_2 \
    --AgentConfig.Env.0.Value true \
    --AgentConfig.Resources.CPU 500m \
    --AgentConfig.Resources.Memory 500Mi \
    --AgentConfig.Ports.0.Name web \
    --AgentConfig.Ports.0.Port 80 \
    --AgentConfig.Ports.0.Protocol TCP \
    --AgentConfig.HealthCheck.HttpGet.Path / \
    --AgentConfig.HealthCheck.HttpGet.Port 80 \
    --AgentConfig.HealthCheck.HttpGet.Scheme HTTP \
    --ProviderConfig.ProviderKind TENCENT_AGS \
    --ProviderConfig.TencentAGS.RoleArn qcs::cam::uin/3321337994:roleName/cos-tcr-full-ags \
    --ProviderConfig.TencentAGS.ImageRegistryType personal \
    --ProviderConfig.TencentAGS.NetworkConfiguration.NetworkMode PUBLIC \
    --DefaultEnvironmentTemplateId envt-6311dafca27b87a106d00045c570e14c
```

Output: 
```
{
    "Response": {
        "AgentVersion": {
            "AgentConfig": {
                "Args": [
                    "-g"
                ],
                "Command": [
                    "nginx"
                ],
                "Env": [
                    {
                        "Name": "TEST_ENV_2",
                        "Value": "true"
                    }
                ],
                "HealthCheck": {
                    "HttpGet": {
                        "Path": "/",
                        "Port": 80,
                        "Scheme": "HTTP"
                    }
                },
                "Image": "ccr.ccs.tencentyun.com/ags.dev/nginx:alpine",
                "Ports": [
                    {
                        "Name": "web",
                        "Port": 80,
                        "Protocol": "TCP"
                    }
                ],
                "Resources": {
                    "CPU": "500m",
                    "Memory": "500Mi"
                }
            },
            "AgentId": "ag-0c6c69201e87d43229f82b485d69311b",
            "CreatedTime": "2026-07-13T07:00:47Z",
            "DefaultEnvironmentTemplateId": "envt-6311dafca27b87a106d00045c570e14c",
            "ProviderConfig": {
                "ProviderKind": "TENCENT_AGS",
                "TencentAGS": {
                    "ImageRegistryType": "personal",
                    "NetworkConfiguration": {
                        "NetworkMode": "PUBLIC"
                    },
                    "RoleArn": "qcs::cam::uin/3321337994:roleName/cos-tcr-full-ags"
                }
            },
            "ProviderStatus": {
                "TencentAGS": {}
            },
            "Status": "CREATING",
            "UpdatedTime": "2026-07-13T07:00:47Z",
            "Version": "v2"
        },
        "RequestId": "73a5aad3-9b81-44d8-b1f5-6615fb8dc769"
    }
}
```

