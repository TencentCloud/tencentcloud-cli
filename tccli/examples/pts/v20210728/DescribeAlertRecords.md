**Example 1: 查询告警历史**



Input: 

```
tccli pts DescribeAlertRecords --cli-unfold-argument  \
    --OrderBy asc \
    --JobIds job-1a2b3c4d \
    --Ascend True \
    --Limit 1 \
    --Offset 1 \
    --ProjectIds project-1a2b3c4d \
    --ScenarioIds scenario-1a2b3c4d
```

Output: 
```
{
    "Response": {
        "AlertRecordSet": [
            {
                "CreatedAt": "2021-12-22T15:04:36+08:00",
                "UpdatedAt": "2021-12-22T15:04:36+08:00",
                "AppId": 13200000,
                "Uin": "13200000",
                "SubAccountUin": "13200000",
                "AlertRecordId": "alert-1a2b3c4d",
                "ProjectId": "project-1a2b3c4d",
                "ScenarioId": "scenario-1a2b3c4d",
                "ScenarioName": "my-scenario",
                "JobId": "job-1a2b3c4d",
                "JobSLAId": "sla-1a2b3c4d",
                "JobSLADescription": "this is a test",
                "Status": {
                    "AbortJob": 1,
                    "SendNotice": 1
                },
                "Target": "target-value"
            }
        ],
        "RequestId": "abc-123-xyz",
        "Total": 1
    }
}
```

