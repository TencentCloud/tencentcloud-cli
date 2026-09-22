**Example 1: 查询 Skill 列表**



Input: 

```
tccli workbuddyenterprise DescribeSkillList --cli-unfold-argument  \
    --Source CUSTOM \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name Keyword \
    --Filters.0.Values 代码
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SkillSet": [
            {
                "Source": "CUSTOM",
                "SkillId": "skill-7f8g9h",
                "Name": "code-review",
                "DisplayName": "代码评审",
                "Description": "按团队规范评审代码改动",
                "Icon": "https://example.com/icon/code-review.png",
                "Enabled": true,
                "DownloadUrl": "https://cos.example.com/skill/code-review-1.2.0.zip",
                "SkillVersion": "1.2.0",
                "CreateTime": "2026-08-11T09:23:10Z",
                "UpdateTime": "2026-09-15T06:51:26Z"
            }
        ],
        "Counts": {
            "Builtin": 12,
            "Custom": 1,
            "Total": 13
        },
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

