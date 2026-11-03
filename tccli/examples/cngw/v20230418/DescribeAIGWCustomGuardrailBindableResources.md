**Example 1: 查看 A2A 资源被其他策略占用**

Supported=true 但 Occupied=true，仍不能直接重复绑定。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli cngw DescribeAIGWCustomGuardrailBindableResources --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --ResourceType agent_api \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "DataList": [
                {
                    "ResourceType": "agent_api",
                    "ResourceId": "55555555-5555-4555-8555-555555555555",
                    "ResourceName": "示例 A2A 服务",
                    "Path": "/agents/example",
                    "Protocol": "a2a",
                    "RouteIds": [
                        "44444444-4444-4444-8444-444444444444"
                    ],
                    "Occupied": true,
                    "Supported": true,
                    "OccupiedBy": "已有审核策略 (11111111-1111-4111-8111-111111111111)"
                }
            ]
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

**Example 2: 编辑时查询可绑定 MCP 资源**

PolicyId 用于排除本策略自己的占用，不表示移除其他策略占用。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli cngw DescribeAIGWCustomGuardrailBindableResources --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --ResourceType mcp_server \
    --PolicyId 11111111-1111-4111-8111-111111111111 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "DataList": [
                {
                    "ResourceType": "mcp_server",
                    "ResourceId": "22222222-2222-4222-8222-222222222222",
                    "ResourceName": "示例 MCP 服务",
                    "Path": "/mcp/example",
                    "Protocol": "mcp",
                    "RouteIds": [
                        "44444444-4444-4444-8444-444444444444"
                    ],
                    "Occupied": false,
                    "Supported": true
                }
            ]
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

