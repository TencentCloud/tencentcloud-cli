**Example 1: MCP Tools批量导入**



Input: 

```
tccli cngw UpdateCloudNativeAPIGatewayMCPTools --cli-unfold-argument  \
    --GatewayId gateway-6fa655a5 \
    --MCPServerId a610d9b2-1b7d-4240-9af0-7761791b3ba1 \
    --Tools.0.Name createPet \
    --Tools.0.DisplayName createPet \
    --Tools.0.Method POST \
    --Tools.0.Description Create a pet \
    --Tools.0.Path /anything \
    --Tools.0.InputParams.0.Name name \
    --Tools.0.InputParams.0.Type string \
    --Tools.0.InputParams.0.Required True \
    --Tools.0.InputParams.0.Position body \
    --Tools.0.InputParams.0.Description Pet name
```

Output: 
```
{
    "Response": {
        "Result": "task-cc6ddf7e",
        "RequestId": "a99ba0dc-68fe-4951-b41b-36a0ccf6ea61"
    }
}
```

