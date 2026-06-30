**Example 1: 查询MCP Server 列表**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPServerList --cli-unfold-argument  \
    --GatewayId gateway-3fbee12c \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "CreateTime": "2026-04-14 17:38:00",
                    "Description": "",
                    "DisplayName": "gitee",
                    "MCPEndpoint": "/mcpservers/gitee/mcp",
                    "Name": "gitee",
                    "RetryCount": 3,
                    "ServerId": "c47474e8-a1f0-4945-8b6e-2364a98beb49",
                    "ServerType": "MCP",
                    "Timeout": 3000,
                    "Transport": "StreamableHttp",
                    "UpdateTime": "2026-04-14 17:38:00",
                    "UpstreamInfo": {
                        "Host": "api.gitee.com",
                        "MCPEndpoint": "/mcp",
                        "Port": 443,
                        "Protocol": "https"
                    },
                    "UpstreamType": "HostIP"
                }
            ],
            "TotalCount": 4
        },
        "RequestId": "39188583-9f3f-42cf-bac1-fdf154f32955"
    }
}
```

