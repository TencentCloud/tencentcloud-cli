**Example 1: 查询实力的可维护时间窗**



Input: 

```
tccli sqlserver DescribeMaintenanceSpan --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5
```

Output: 
```
{
    "Response": {
        "RequestId": "160c730d-b563-4a43-b377-428191d77f39",
        "Span": 6,
        "StartTime": "00:00",
        "Weekly": [
            1
        ]
    }
}
```

