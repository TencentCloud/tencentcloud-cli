**Example 1: 成功**

 

Input: 

```
tccli iss AddRecordBackupTemplate --cli-unfold-argument  \
    --TemplateName 123456 \
    --TimeSections.0.DayOfWeek 4 \
    --TimeSections.0.StartTime 00:00:00 \
    --TimeSections.0.EndTime 02:00:00 \
    --DevTimeSections.0.DayOfWeek 3 \
    --DevTimeSections.0.StartTime 00:00:00 \
    --DevTimeSections.0.EndTime 01:00:00 \
    --Scale 1
```

Output: 
```
{
    "Response": {}
}
```

