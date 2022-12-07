**Example 1: 示例**



Input: 

```
tccli cdwch CreateBackUpSchedule --cli-unfold-argument  \
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
    --WeekDays 2 \
    --ExecuteHour 1 \
    --ScheduleId 4879
```

Output: 
```
{
    "Response": {
        "RequestId": "111"
    }
}
```

