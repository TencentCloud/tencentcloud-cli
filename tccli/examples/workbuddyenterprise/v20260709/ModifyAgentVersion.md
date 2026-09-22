**Example 1: 修改 Agent 版本**



Input: 

```
tccli workbuddyenterprise ModifyAgentVersion --cli-unfold-argument  \
    --AgentId 736918300000000001 \
    --VersionId 2087791755109965827 \
    --Model hunyuan-turbos-latest \
    --Description 调整系统提示词，收紧回答范围
```

Output: 
```
{
    "Response": {
        "VersionId": "2087791755109965827",
        "AgentId": "736918300000000001",
        "VersionName": "default",
        "VersionType": "DEFAULT",
        "Description": "调整系统提示词，收紧回答范围",
        "Model": "hunyuan-turbos-latest",
        "Manifest": "{\"version\":\"2.0\",\"system_prompt\":\"你是数据分析助手，负责汇总运营数据。\"}",
        "Status": "ENABLED",
        "CreatedTime": "2026-07-20T07:10:00Z",
        "ModifiedTime": "2026-08-10T15:30:00Z",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

