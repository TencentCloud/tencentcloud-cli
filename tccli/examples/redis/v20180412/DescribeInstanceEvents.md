**Example 1: 查询实例事件**

查询实例事件

Input: 

```
tccli redis DescribeInstanceEvents --cli-unfold-argument  \
    --InstanceId crs-b6wst31p \
    --PageSize 20 \
    --PageNo 1 \
    --ExecutionStartDate 2023-10-04 \
    --ExecutionEndDate 2023-10-04 \
    --Grades Low \
    --Status Waiting \
    --EventTypes InstanceMigration
```

Output: 
```
{
    "Response": {
        "RedisInstanceEvents": [
            {
                "EffectInfo": "迁移完成时会有一次秒级别的闪断",
                "EndTime": "22:00",
                "ExecutionDate": "2023-09-18",
                "Grade": "Low",
                "ID": 10,
                "InitialExecutionDate": "2023-08-19",
                "InstanceId": "crs-b6wst31p",
                "InstanceName": "benyqhuang8",
                "LatestExecutionDate": "2023-09-18",
                "StartTime": "21:00",
                "Status": "Waiting",
                "TaskEndTime": "0000-00-00 00:00:00",
                "Type": "InstanceMigration"
            }
        ],
        "RequestId": "36a33a3d-f9ce-47c1-87d0-84869a37466d",
        "TotalCount": 1
    }
}
```

