**Example 1: 发起智能诊断对话**



Input: 

```
tccli cloudmate CloudMateAgent --cli-unfold-argument  \
    --WorkspaceId bd225f0e-8a75-4bd7-8bc3-99b026b41256 \
    --Message 你是谁 \
    --ScenarioId d824d96c-7c07-4f6a-aef6-2f14a9fafb1e
```

Output: 
```
{
    "SessionId": "46be4923-6f58-4ccb-8a26-6f56aad4a17b",
    "Timestamp": 1766561543,
    "Content": {
        "Role": "model_output",
        "Parts": [
            {
                "Text": "我是 CloudMate，一个专注于帮助您解决云平台问题的 AI 助手。您可以随时向我描述您遇到的问题。"
            }
        ]
    },
    "Partial": false,
    "TurnComplete": true
}
```

