**Example 1: 获取技能列表**



Input: 

```
tccli tcr ListSkills --cli-unfold-argument  \
    --RegistryId tcr-kpfrletb \
    --Status active \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "SkillList": [
            {
                "Description": "cache-manager - MCP Server powered by node20",
                "LatestVersion": "2.0.0",
                "SkillName": "cache-manager",
                "SkillType": "MCP Server",
                "Status": "active",
                "Tags": [
                    "mcp"
                ],
                "UpdateTime": "2026-03-24T07:43:14.042Z"
            }
        ],
        "TotalCount": 21,
        "RequestId": "14c8656f-4b09-4764-8a10-3a16eeae8932"
    }
}
```

