**Example 1: 示例**

创建或者修改备份策略

Input: 

```
tccli cdwch CreateBackUpSchedule --cli-unfold-argument  \
    --InstanceId cdwch-1vud9x9x \
    --ScheduleType data \
    --OperationType update \
    --BackUpTables.0.Database default \
    --BackUpTables.0.Table customer \
    --BackUpTables.0.Ips 172.16.4.17 \
    --BackUpTables.0.TotalBytes 1203976330 \
    --BackUpTables.0.VCluster default_cluster \
    --BackUpTables.1.Database default \
    --BackUpTables.1.Table lineorder \
    --BackUpTables.1.Ips 172.16.4.17 \
    --BackUpTables.1.TotalBytes 179936234797 \
    --BackUpTables.1.VCluster default_cluster \
    --RetainDays 7 \
    --WeekDays 2 \
    --ExecuteHour 1 \
    --ScheduleId 4879
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

