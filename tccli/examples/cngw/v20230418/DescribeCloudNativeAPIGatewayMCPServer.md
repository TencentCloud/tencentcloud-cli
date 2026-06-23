**Example 1: 查看MCPServer 详情**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPServer --cli-unfold-argument  \
    --GatewayId gateway-545fe799 \
    --ServerId 667065f5-6796-4430-b987-9a8b43c3d5b1
```

Output: 
```
{
    "Response": {
        "Result": {
            "CreateTime": "2026-04-15 16:50:50",
            "Description": "",
            "DisplayName": "giteeasd",
            "MCPEndpoint": "/mcpservers/gitee/mcp",
            "Name": "gitee",
            "RetryCount": 3,
            "ServerId": "667065f5-6796-4430-b987-9a8b43c3d5b1",
            "ServerType": "MCP",
            "Timeout": 3000,
            "Transport": "StreamableHttp",
            "UpdateTime": "2026-04-15 16:54:34",
            "UpstreamInfo": {
                "Host": "api.gitee.com",
                "MCPEndpoint": "/mcp",
                "Port": 443,
                "Protocol": "https"
            },
            "UpstreamType": "HostIP"
        },
        "RequestId": "98535882-57b3-4f26-a506-a3ce68d2269b"
    }
}
```

