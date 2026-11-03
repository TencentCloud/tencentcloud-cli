**Example 1: 查询支持的能力及默认限制**

能力中的超时默认值为 500 ms；请勿把本示例的 Limits 当成 Create/Modify 入参。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli cngw DescribeAIGWCustomGuardrailCapabilities --cli-unfold-argument  \
    --GatewayId gateway-12345678
```

Output: 
```
{
    "Response": {
        "Result": {
            "MinGatewayVersion": "3.9.6",
            "SupportedResourceTypes": [
                "model_api",
                "mcp_server",
                "agent_api"
            ],
            "SupportedProtocols": [
                "openai",
                "anthropic",
                "a2a",
                "mcp"
            ],
            "SupportedDirections": [
                "input",
                "both"
            ],
            "SupportsStreaming": true,
            "SupportsFieldMapping": true,
            "DefaultBlockMessage": "您的请求可能包含不安全内容，已被安全策略拦截。请修改后重试。",
            "MaxBlockMessageLength": 512,
            "Limits": {
                "MaxHeaderAllowList": 64,
                "MaxKeywordsPerDirection": 64,
                "InlineBodyBytes": 1048576,
                "MaxAcceptedBodyBytes": 33554432,
                "TransferChunkBytes": 262144,
                "MaxTransferChunkBytes": 4194304,
                "TransferTargetMaxChunks": 32,
                "MaxResponseBodyBytes": 10485760,
                "MaxStreamEventBytes": 262144,
                "StreamRelayMaxConcurrentRequests": 512,
                "MinTimeoutMs": 50,
                "MaxTimeoutMs": 5000,
                "DefaultTimeoutMs": 500
            }
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

