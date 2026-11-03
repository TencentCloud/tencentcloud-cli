**Example 1: 关闭审核引擎鉴权并清除旧密钥**

只修改网关访问审核引擎的鉴权，不关闭客户端访问网关的鉴权。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse ModifyAIGWCustomGuardrailPolicy --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --PolicyId 11111111-1111-4111-8111-111111111111 \
    --AuthConfig.AuthType none \
    --AuthConfig.ClearApiKey True
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "Policy": {
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
            },
            "AddedResources": [
                {
                    "ResourceType": "mcp_server",
                    "ResourceId": "22222222-2222-4222-8222-222222222222"
                }
            ],
            "RemovedCount": 0,
            "FailedResources": [],
            "SyncStatus": "synced"
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

**Example 2: 开启响应审核与内容改写**

以已有 field_mapping 策略为前提，未传的审核地址、命中字段与其他配置保留。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse ModifyAIGWCustomGuardrailPolicy --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --PolicyId 11111111-1111-4111-8111-111111111111 \
    --BehaviorConfig.Direction both \
    --DecisionConfig.RewriteEnabled True \
    --DecisionConfig.FieldMapping.RewriteFieldPath content.body
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "Policy": {
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
                    "RewriteEnabled": true,
                    "FieldMapping": {
                        "HitFieldPath": "decision",
                        "HitValue": "\"block\"",
                        "MessageFieldPath": "message",
                        "RewriteFieldPath": "content.body"
                    }
                },
                "BehaviorConfig": {
                    "Direction": "both",
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
            },
            "AddedResources": [
                {
                    "ResourceType": "mcp_server",
                    "ResourceId": "22222222-2222-4222-8222-222222222222"
                }
            ],
            "RemovedCount": 0,
            "FailedResources": [],
            "SyncStatus": "synced"
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

**Example 3: 设置全局资源范围与 10% 采样**

假定网关当前仅有示例 MCP 这一项受支持资源且未被其他策略占用。global 不填写资源列表；采样率 0.1 为 10%，未抽中内容不送审。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse ModifyAIGWCustomGuardrailPolicy --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --PolicyId 11111111-1111-4111-8111-111111111111 \
    --Scope.BindType global \
    --FilterConfig.SamplingEnabled True \
    --FilterConfig.RequestSamplingRate 0.1 \
    --FilterConfig.ResponseSamplingRate 0.1
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "Policy": {
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
                    "SamplingEnabled": true,
                    "RequestSamplingRate": 0.1,
                    "ResponseSamplingRate": 0.1
                },
                "Scope": {
                    "BindType": "global",
                    "Resources": []
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
            },
            "AddedResources": [
                {
                    "ResourceType": "mcp_server",
                    "ResourceId": "22222222-2222-4222-8222-222222222222"
                }
            ],
            "RemovedCount": 0,
            "FailedResources": [],
            "SyncStatus": "synced"
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

