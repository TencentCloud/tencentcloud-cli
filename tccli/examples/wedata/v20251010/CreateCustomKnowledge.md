**Example 1: 创建自定义知识，注意 jsondata 中要和字段保持一致**



Input: 

```
tccli wedata CreateCustomKnowledge --cli-unfold-argument  \
    --WorkspaceId 1 \
    --KnowledgeBaseName qizhi_test \
    --KnowledgeId 2 \
    --JsonData {"key": "monthly_active_users"}
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorCode": 0,
            "ErrorMessage": ""
        },
        "RequestId": "c4745ff1-6e8b-49fb-b75d-6e9bfe61e30e"
    }
}
```

