**Example 1: 创建MCP Server**



Input: 

```
tccli cngw CreateCloudNativeAPIGatewayMCPServer --cli-unfold-argument  \
    --GatewayId gateway-27268511 \
    --Name test-virtual-mcp-2 \
    --DisplayName 虚拟MCP \
    --ServerType Rest2MCP \
    --Transport StreamableHttp \
    --UpstreamType VirtualMCPServer \
    --Timeout 3000 \
    --RetryCount 3 \
    --Description 虚拟MCP服务 \
    --EnableHealthCheck False
```

Output: 
```
{
    "Response": {
        "Result": {
            "ID": "deae9637-1fb1-46cf-8c14-cab71114a2b9",
            "Success": true
        },
        "RequestId": "aacffe14-af80-4969-90ff-d945cfe44464"
    }
}
```

