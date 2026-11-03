**Example 1: 分页查询响应审核记录**

时间为示例固定区间，实际调用请替换为目标请求发生时间，并确认日志已投递至 CLS。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli cngw DescribeAIGWCustomGuardrailHits --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --StartTime 1788832800 \
    --EndTime 1788836400 \
    --Filters.0.Name PolicyId \
    --Filters.0.Values 11111111-1111-4111-8111-111111111111 \
    --Filters.1.Name Direction \
    --Filters.1.Values response \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "Hits": [
                {
                    "RequestId": "77777777-7777-4777-8777-777777777777",
                    "Timestamp": 1788833100123,
                    "GatewayId": "gateway-12345678",
                    "PolicyId": "11111111-1111-4111-8111-111111111111",
                    "PolicyName": "mcp-custom-audit",
                    "ResourceType": "mcp_server",
                    "ResourceId": "22222222-2222-4222-8222-222222222222",
                    "RouteId": "44444444-4444-4444-8444-444444444444",
                    "Protocol": "mcp-streamable-http",
                    "Direction": "response",
                    "Streaming": true,
                    "Final": false,
                    "Decision": "block",
                    "ConfiguredAction": "block",
                    "EffectiveAction": "block",
                    "Rewritten": false,
                    "Blocked": true,
                    "Downgraded": false,
                    "ProviderStatusCode": 200,
                    "LatencyMs": 52.3
                }
            ],
            "Truncated": false
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

