**Example 1: 创建 Agent 版本**



Input: 

```
tccli workbuddyenterprise CreateAgentVersion --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --Model hunyuan-turbos-latest \
    --Description 接入数据查询技能 \
    --Manifest {"version":"2.0","system_prompt":"你是数据分析助手，负责汇总运营数据。"}
```

Output: 
```
{
    "Response": {
        "VersionId": "2087791755109965825",
        "AgentId": "736918300000000001",
        "VersionName": "prod-3",
        "VersionType": "PROD",
        "Description": "接入数据查询技能",
        "Model": "hunyuan-turbos-latest",
        "Manifest": "{\"version\":\"2.0\",\"system_prompt\":\"你是数据分析助手，负责汇总运营数据。\"}",
        "Status": "ENABLED",
        "CreatedTime": "2026-08-01T10:00:00Z",
        "ModifiedTime": "2026-08-01T10:00:00Z",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

