**Example 1: 创建智能体**



Input: 

```
tccli iotexplorer CreateTWeTalkAIBot --cli-unfold-argument  \
    --Name 示例bot \
    --BotType mobile_app \
    --RAGConfig {
  "RAGEnabled": true,
  "KnowledgeBaseId": "kb-test-001",
  "RAGRegion": "ap-guangzhou",
  "RAGTopK": 5,
  "RAGScoreThreshold": 0.75,
  "RAGRoleExternalId": "external-id-demo",
  "RAGRoleDurationSeconds": 3600
}
```

Output: 
```
{
    "Response": {
        "BotId": "bot-PuzbxMQnHk",
        "RequestId": "91229769-ffe1-4a44-963c-9da03517d3ae"
    }
}
```

