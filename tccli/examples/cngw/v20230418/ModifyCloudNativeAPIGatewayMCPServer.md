**Example 1: 修改MCP 服务**



Input: 

```
tccli cngw ModifyCloudNativeAPIGatewayMCPServer --cli-unfold-argument  \
    --GatewayId gateway-c67671ec \
    --DisplayName dev \
    --ServerId d49b1959-f847-4012-8af8-e286aa360ee8 \
    --UpstreamType HostIP \
    --Timeout 3000 \
    --RetryCount 3 \
    --UpstreamInfo.ServiceId 4e141ac6-f0cd-4d35-80f0-75e47f5d56a6 \
    --Description 开发 mcp
```

Output: 
```
{
    "Response": {
        "RequestId": "f3d825c4-8ef1-4209-accf-f18e615c3923"
    }
}
```

