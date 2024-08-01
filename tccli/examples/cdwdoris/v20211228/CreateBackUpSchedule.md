**Example 1: 示例**



Input: 

```
tccli cdwdoris CreateBackUpSchedule --cli-unfold-argument  \
    --ScheduleId 0 \
    --WeekDays 1 \
    --BackUpTables.0.Table 1 \
    --BackUpTables.0.TotalBytes 0 \
    --BackUpTables.0.Database 1 \
    --ExecuteHour 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1"
    }
}
```

