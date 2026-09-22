**Example 1: 基于源版本创建 Agent 版本**



Input: 

```
tccli workbuddyenterprise CreateAgentVersionFromSource --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --SourceVersionId 2087791755109965825 \
    --Model hunyuan-turbos-latest \
    --Description 在 prod-3 基础上调整系统提示词
```

Output: 
```
{
    "Response": {
        "VersionId": "2087791755109965826",
        "AgentId": "736918300000000001",
        "VersionName": "test-3",
        "VersionType": "TEST",
        "Description": "在 prod-3 基础上调整系统提示词",
        "Model": "hunyuan-turbos-latest",
        "Manifest": "{\"version\":\"2.0\",\"system_prompt\":\"你是数据分析助手，负责汇总运营数据。\"}",
        "Status": "ENABLED",
        "CreatedTime": "2026-08-12T08:20:00Z",
        "ModifiedTime": "2026-08-12T08:20:00Z",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

