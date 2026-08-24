**Example 1: 查询MCP Server 列表**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPServerList --cli-unfold-argument  \
    --GatewayId gateway-9a766f25 \
    --Limit 10 \
    --Offset 0 \
    --SecretKeyId secret-f60091e9e0a43e
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "ConflictStrategy": "",
                    "CreateTime": "2026-08-14 17:45:15",
                    "Description": "",
                    "DisplayName": "测试测试",
                    "EnableHealthCheck": false,
                    "HealthCheck": null,
                    "MCPEndpoint": "/mcpservers/testtest/mcp",
                    "MarketStatus": "None",
                    "Name": "testtest",
                    "PreserveHost": false,
                    "RetryCount": 3,
                    "ServerId": "c11e82a4-15f3-4107-83d3-a655e2213790",
                    "ServerType": "MCP",
                    "SessionConfig": {
                        "SessionStorage": "memory"
                    },
                    "Status": "Online",
                    "Timeout": 3000,
                    "ToolCountLimit": 0,
                    "Transport": "StreamableHttp",
                    "UpdateTime": "2026-08-14 17:45:15",
                    "UpstreamInfo": {
                        "Host": "www.tencent.com",
                        "MCPEndpoint": "/mcp",
                        "Port": 8997,
                        "Protocol": "https",
                        "TLSConfig": {
                            "ClientCertId": "bf6ff0bf-737e-49ef-85ab-2ee71c45ac14",
                            "TLSVerify": true,
                            "UpstreamCACertIds": [
                                "c4b5d580-1a93-4747-a120-5b6eef6682f7"
                            ]
                        }
                    },
                    "UpstreamType": "HostIP"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "b55b1ad0-9452-4ae0-befa-23d3d9701a03"
    }
}
```

