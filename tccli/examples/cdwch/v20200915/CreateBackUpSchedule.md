**Example 1: 示例**



Input: 

```
tccli cdwch CreateBackUpSchedule --cli-unfold-argument  \
    --ScheduleId 0 \
    --WeekDays xx \
    --BackUpTables.0.Table xx \
    --BackUpTables.0.VCluster xx \
    --BackUpTables.0.TotalBytes 0 \
    --BackUpTables.0.Database xx \
    --ExecuteHour 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

