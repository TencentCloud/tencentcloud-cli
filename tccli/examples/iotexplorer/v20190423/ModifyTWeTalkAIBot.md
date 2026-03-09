**Example 1: 修改智能体**



Input: 

```
tccli iotexplorer ModifyTWeTalkAIBot --cli-unfold-argument  \
    --BotId bot-PuzbxMQnHk \
    --RAGConfig {
  "RAGEnabled": true,
  "KnowledgeBaseId": "kb-test-001",
  "RAGRegion": "ap-guangzhou",
  "RAGTopK": 5,
  "RAGScoreThreshold": 0.75,
  "RAGRoleExternalId": "external-id-demo",
  "RAGRoleDurationSeconds": 1600
}
```

Output: 
```
{
    "Response": {
        "RequestId": "9e74b195-eb4b-4335-9693-1cd74bd807c4"
    }
}
```

