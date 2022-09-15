**Example 1: 查询快照操作日志**



Input: 

```
tccli cfs DescribeSnapshotOperationLogs --cli-unfold-argument  \
    --SnapshotId snapcfs-12345 \
    --EndTime 2021-08-12 20:50:45 \
    --StartTime 2021-08-11 20:50:45
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "SnapshotId": "snapcfs-12345",
        "SnapshotOperates": [
            {
                "Action": "UpdateCfsSnapshotAttribute",
                "ActionTime": "2021-08-13 20:03:28",
                "ActionName": "UpdateCfsSnapshotAttribute",
                "Operator": "",
                "Result": 2
            }
        ]
    }
}
```

