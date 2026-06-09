**Example 1: 获取技能详情**



Input: 

```
tccli tcr DescribeSkillDetail --cli-unfold-argument  \
    --RegistryId tcr-kpfrletb \
    --SkillName cache-manager \
    --SkillVersion 2.0.0
```

Output: 
```
{
    "Response": {
        "Skill": {
            "Description": "cache-manager - MCP Server powered by node20",
            "Runtime": "node20",
            "SkillName": "cache-manager",
            "SkillType": "MCP Server",
            "SkillVersion": "2.0.0",
            "Status": "active",
            "Tags": [
                "mcp"
            ],
            "UpdateTime": "2026-03-24T07:43:14.042Z"
        },
        "RequestId": "55dba911-617b-45a8-b7ff-3b21e774a890"
    }
}
```

