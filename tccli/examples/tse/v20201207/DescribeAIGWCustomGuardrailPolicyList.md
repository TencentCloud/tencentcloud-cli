**Example 1: 分页查询已启用且同步成功的策略**

Filters.Values 是字符串数组。继续查询时递增 Offset。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse DescribeAIGWCustomGuardrailPolicyList --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --Limit 20 \
    --Offset 0 \
    --Keyword mcp \
    --Filters.0.Name Enabled \
    --Filters.0.Values true \
    --Filters.1.Name SyncStatus \
    --Filters.1.Values synced
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "DataList": [
                {
                    "PolicyId": "11111111-1111-4111-8111-111111111111",
                    "Name": "mcp-custom-audit",
                    "Description": "MCP Streamable HTTP 输入审核",
                    "Enabled": true,
                    "EffectiveEnabled": true,
                    "ServiceConfig": {
                        "AddressMode": "manual",
                        "Endpoint": "https://audit.example.com/v2/audit",
                        "SSLVerify": true,
                        "QueryPassthroughEnabled": false,
                        "HeaderAllowList": []
                    },
                    "AuthConfig": {
                        "AuthType": "none",
                        "HasApiKey": false
                    },
                    "DecisionConfig": {
                        "ContractMode": "field_mapping",
                        "BlockMessageMode": "response",
                        "BlockMessage": "您的请求可能包含不安全内容，已被安全策略拦截。请修改后重试。",
                        "RewriteEnabled": false,
                        "FieldMapping": {
                            "HitFieldPath": "decision",
                            "HitValue": "\"block\"",
                            "MessageFieldPath": "message"
                        }
                    },
                    "BehaviorConfig": {
                        "Direction": "input",
                        "HandleAction": "block",
                        "TimeoutMs": 5000,
                        "FailureMode": "closed"
                    },
                    "FilterConfig": {
                        "RequestStreamMode": "all",
                        "ResponseStreamMode": "all",
                        "RequestKeywords": [],
                        "ResponseKeywords": [],
                        "KeywordMatchMode": "any",
                        "KeywordCaseSensitive": false,
                        "SamplingEnabled": false,
                        "RequestSamplingRate": 1,
                        "ResponseSamplingRate": 1
                    },
                    "Scope": {
                        "BindType": "resource",
                        "Resources": [
                            {
                                "ResourceType": "mcp_server",
                                "ResourceId": "22222222-2222-4222-8222-222222222222"
                            }
                        ]
                    },
                    "Bindings": [
                        {
                            "ResourceType": "mcp_server",
                            "ResourceId": "22222222-2222-4222-8222-222222222222",
                            "ResourceName": "示例 MCP 服务",
                            "Path": "/mcp/example",
                            "Protocol": "mcp",
                            "RouteId": "44444444-4444-4444-8444-444444444444",
                            "PluginId": "88888888-8888-4888-8888-888888888888",
                            "SyncStatus": "synced"
                        }
                    ],
                    "SyncStatus": "synced",
                    "CreateTime": "2026-09-08 10:00:00",
                    "ModificationTime": "2026-09-08 10:00:00"
                }
            ]
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

