**Example 1: 获取迁移任务列表**



Input: 

```
tccli trocket DescribeSmoothMigrationTaskList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "Data": [
            {
                "TaskId": "abc",
                "TaskName": "test",
                "SourceClusterName": "Test",
                "InstanceId": "rmq-xxxxx",
                "ConnectionType": "VPC",
                "SourceNameServer": "1.1.1.1:9876",
                "TaskStatus": "ServiceMigration",
                "InstanceVersion": "5"
            }
        ],
        "RequestId": "abc"
    }
}
```

