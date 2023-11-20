**Example 1: 查询回档任务列表**

查询回档任务列表

Input: 

```
tccli sqlserver DescribeRestoreTask --cli-unfold-argument  \
    --InstanceId mssql-aju981jo \
    --RestoreType 0 \
    --TargetRegion ap-shanghai \
    --TargetType 2 \
    --Status 1 \
    --StartTime 2023-04-12: 00:00:00 \
    --EndTime 2023-04-12: 00:00:00 \
    --Offset 0 \
    --Limit 10 \
    --OrderBy startTime \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "RequestId": "88310080-925d-11ed-981b-c7bf72df626c",
        "Tasks": [
            {
                "TargetInstanceId": "mssql-892932uiu",
                "TargetInstanceName": "test",
                "TargetInstanceStatus": 2,
                "TargetRegion": "ap-guangzhou",
                "TargetType": 0,
                "EndTime": "0000-00-00 00:00:00",
                "RestoreId": 1012,
                "RestoreTime": "2023-01-12 16:22:48",
                "RestoreType": 0,
                "StartTime": "2023-01-12 16:22:55",
                "Status": 0
            }
        ],
        "TotalCount": 1
    }
}
```

