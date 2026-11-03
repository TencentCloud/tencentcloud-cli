**Example 1: 创建 MCP 输入审核策略（自定义映射、无鉴权）**

审核引擎返回 {"decision":"block","message":"示例风险提示"} 时命中，返回 {"decision":"allow"} 时不命中。失败关闭和 5000 ms 均为显式示例值。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse CreateAIGWCustomGuardrailPolicy --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --Name mcp-custom-audit \
    --Description MCP Streamable HTTP 输入审核 \
    --Enabled True \
    --ServiceConfig.AddressMode manual \
    --ServiceConfig.Endpoint https://audit.example.com/v2/audit \
    --ServiceConfig.SSLVerify True \
    --ServiceConfig.QueryPassthroughEnabled False \
    --AuthConfig.AuthType none \
    --DecisionConfig.ContractMode field_mapping \
    --DecisionConfig.BlockMessageMode response \
    --DecisionConfig.BlockMessage 您的请求可能包含不安全内容，已被安全策略拦截。请修改后重试。 \
    --DecisionConfig.RewriteEnabled False \
    --DecisionConfig.FieldMapping.HitFieldPath decision \
    --DecisionConfig.FieldMapping.HitValue "block" \
    --DecisionConfig.FieldMapping.MessageFieldPath message \
    --BehaviorConfig.Direction input \
    --BehaviorConfig.HandleAction block \
    --BehaviorConfig.TimeoutMs 5000 \
    --BehaviorConfig.FailureMode closed \
    --FilterConfig.RequestStreamMode all \
    --FilterConfig.ResponseStreamMode all \
    --FilterConfig.KeywordMatchMode any \
    --FilterConfig.KeywordCaseSensitive False \
    --FilterConfig.SamplingEnabled False \
    --FilterConfig.RequestSamplingRate 1 \
    --FilterConfig.ResponseSamplingRate 1 \
    --Scope.BindType resource \
    --Scope.Resources.0.ResourceType mcp_server \
    --Scope.Resources.0.ResourceId 22222222-2222-4222-8222-222222222222
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "PolicyId": "11111111-1111-4111-8111-111111111111",
            "AddedResources": [
                {
                    "ResourceType": "mcp_server",
                    "ResourceId": "22222222-2222-4222-8222-222222222222"
                }
            ],
            "FailedResources": [],
            "SyncStatus": "synced"
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

**Example 2: 创建模型流式输出审核策略**

审核输入及流式输出。若输出审核时引擎返回 content.body，值应为完整 SSE 事件文本，替换当前审核批次；不是把任意自然语言字符串直接当作模型响应。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse CreateAIGWCustomGuardrailPolicy --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --Name llm-stream-audit \
    --Description 模型 SSE 响应审核 \
    --Enabled True \
    --ServiceConfig.AddressMode manual \
    --ServiceConfig.Endpoint https://audit.example.com/v2/audit \
    --ServiceConfig.SSLVerify True \
    --ServiceConfig.QueryPassthroughEnabled False \
    --AuthConfig.AuthType none \
    --DecisionConfig.ContractMode field_mapping \
    --DecisionConfig.BlockMessageMode response \
    --DecisionConfig.BlockMessage 您的请求可能包含不安全内容，已被安全策略拦截。请修改后重试。 \
    --DecisionConfig.RewriteEnabled True \
    --DecisionConfig.FieldMapping.HitFieldPath decision \
    --DecisionConfig.FieldMapping.HitValue "block" \
    --DecisionConfig.FieldMapping.MessageFieldPath message \
    --DecisionConfig.FieldMapping.RewriteFieldPath content.body \
    --BehaviorConfig.Direction both \
    --BehaviorConfig.HandleAction block \
    --BehaviorConfig.TimeoutMs 5000 \
    --BehaviorConfig.FailureMode closed \
    --FilterConfig.RequestStreamMode all \
    --FilterConfig.ResponseStreamMode streaming \
    --FilterConfig.KeywordMatchMode any \
    --FilterConfig.KeywordCaseSensitive False \
    --FilterConfig.SamplingEnabled False \
    --FilterConfig.RequestSamplingRate 1 \
    --FilterConfig.ResponseSamplingRate 1 \
    --Scope.BindType resource \
    --Scope.Resources.0.ResourceType model_api \
    --Scope.Resources.0.ResourceId 66666666666646668666666666666666
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "PolicyId": "11111111-1111-4111-8111-111111111111",
            "AddedResources": [
                {
                    "ResourceType": "model_api",
                    "ResourceId": "66666666666646668666666666666666"
                }
            ],
            "FailedResources": [],
            "SyncStatus": "synced"
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

**Example 3: 引用已配置审核服务，创建 A2A 双向审核与输出改写**

服务的 path 需已配置为审核接口路径。引擎正常响应带有 content.body 时，输出方向优先替换；输入方向只按命中规则判断是否阻断。Bearer 值使用审核引擎自己的令牌，不是网关客户端密钥。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse CreateAIGWCustomGuardrailPolicy --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --Name a2a-custom-audit \
    --Description A2A 输入输出审核 \
    --Enabled True \
    --ServiceConfig.AddressMode service \
    --ServiceConfig.ServiceId 33333333-3333-4333-8333-333333333333 \
    --ServiceConfig.SSLVerify True \
    --AuthConfig.AuthType api_key \
    --AuthConfig.HeaderName Authorization \
    --AuthConfig.ApiKey Bearer <AUDIT_ENGINE_TOKEN> \
    --DecisionConfig.ContractMode field_mapping \
    --DecisionConfig.BlockMessageMode response \
    --DecisionConfig.BlockMessage 您的请求可能包含不安全内容，已被安全策略拦截。请修改后重试。 \
    --DecisionConfig.RewriteEnabled True \
    --DecisionConfig.FieldMapping.HitFieldPath decision \
    --DecisionConfig.FieldMapping.HitValue "block" \
    --DecisionConfig.FieldMapping.MessageFieldPath message \
    --DecisionConfig.FieldMapping.RewriteFieldPath content.body \
    --BehaviorConfig.Direction both \
    --BehaviorConfig.HandleAction block \
    --BehaviorConfig.TimeoutMs 5000 \
    --BehaviorConfig.FailureMode closed \
    --FilterConfig.RequestStreamMode all \
    --FilterConfig.ResponseStreamMode all \
    --FilterConfig.KeywordMatchMode any \
    --FilterConfig.KeywordCaseSensitive False \
    --FilterConfig.SamplingEnabled False \
    --FilterConfig.RequestSamplingRate 1 \
    --FilterConfig.ResponseSamplingRate 1 \
    --Scope.BindType resource \
    --Scope.Resources.0.ResourceType agent_api \
    --Scope.Resources.0.ResourceId 55555555-5555-4555-8555-555555555555
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "PolicyId": "11111111-1111-4111-8111-111111111111",
            "AddedResources": [
                {
                    "ResourceType": "agent_api",
                    "ResourceId": "55555555-5555-4555-8555-555555555555"
                }
            ],
            "FailedResources": [],
            "SyncStatus": "synced"
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

