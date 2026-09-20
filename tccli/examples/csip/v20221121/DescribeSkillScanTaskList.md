**Example 1: 查询 Skill 扫描任务列表**



Input: 

```
tccli csip DescribeSkillScanTaskList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --StartTime 2026-08-01 00:00:00 \
    --EndTime 2026-08-26 23:59:59
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TaskList": [
            {
                "InsertTime": "2026-08-20T10:30:00+08:00",
                "SkillName": "git-helper",
                "DeductCount": 37
            },
            {
                "InsertTime": "2026-08-15T09:00:00+08:00",
                "SkillName": "code-review",
                "DeductCount": 12
            }
        ],
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

