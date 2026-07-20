**Example 1: 查询部署日志**



Input: 

```
tccli teo DescribeInferenceServiceDeploymentLogs --cli-unfold-argument  \
    --ZoneId zone-3jxerasahh8l \
    --ServiceId inf-nm***s7c2xq4 \
    --RecordId inf-nmlxt***2xq4-lifm9n8c \
    --StartTime 2026-02-10T10:10:40Z \
    --EndTime 2026-02-11T16:40:50Z \
    --SortBy timestamp \
    --SortOrder asc \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "DeploymentLogInfoSet": [
            {
                "LogMessage": "Initiating container image synchronization to edge computing nodes",
                "Timestamp": "2026-02-11T08:12:30Z"
            }
        ],
        "TotalCount": 2,
        "RequestId": "df2d51bf-d6fd-4c5b-8377-ef00dcd9ce80"
    }
}
```

