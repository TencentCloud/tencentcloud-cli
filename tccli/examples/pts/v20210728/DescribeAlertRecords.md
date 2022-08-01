**Example 1: 查询告警历史**



Input: 

```
tccli pts DescribeAlertRecords --cli-unfold-argument  \
    --OrderBy xx \
    --JobIds xx \
    --Ascend True \
    --Limit 1 \
    --Offset 1 \
    --ProjectIds xx \
    --ScenarioIds xx
```

Output: 
```
{
    "Response": {
        "AlertRecordSet": [
            {
                "CreatedAt": "2021-12-22T15:04:36+08:00",
                "UpdatedAt": "2021-12-22T15:04:36+08:00",
                "AlertRecordId": "alert-q5qn20zy",
                "ProjectId": "project-cphgtuvq",
                "ScenarioId": "scenario-lkbg8f20",
                "JobId": "job-b8eklbx8",
                "Status": 1
            }
        ],
        "RequestId": "9g7dz8hd4f6xp1fnx4izhfyad1tz2ke-",
        "Total": 1
    }
}
```

