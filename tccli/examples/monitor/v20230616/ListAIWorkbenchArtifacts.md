**Example 1: 测试环境真实示例**



Input: 

```
tccli monitor ListAIWorkbenchArtifacts --cli-unfold-argument  \
    --PerPage 10 \
    --PageNo 1 \
    --SessionIds ses-************
```

Output: 
```
{
    "Response": {
        "Artifacts": [
            {
                "AgentId": "agt-fl41a45q",
                "ArtifactId": "a3ad713a514a00056779f487fb1b51b2",
                "CreatedAt": 0,
                "IsGlobal": false,
                "MimeType": "application/json",
                "Name": "custom_rules.json",
                "SizeBytes": 646,
                "SkillId": "skl-183na51w",
                "StoragePath": "sandbox_file://ses-gqohe600bjp2/custom_rules.json",
                "UpdatedAt": 0
            }
        ],
        "PageResult": {
            "CurrentPageNo": 1,
            "TotalCount": 3,
            "TotalPage": 1
        },
        "RequestId": "b3bd2b5f-c268-46ea-8644-a37add135bba"
    }
}
```

