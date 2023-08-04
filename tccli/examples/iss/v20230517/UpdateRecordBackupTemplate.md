**Example 1: 成功**

 

Input: 

```
tccli iss UpdateRecordBackupTemplate --cli-unfold-argument  \
    --TemplateId abcdefgh-1234-5678-ijkl-1234567890ab \
    --Mod.TimeSections.0.DayOfWeek 2 \
    --Mod.TimeSections.0.StartTime 00:00:00 \
    --Mod.TimeSections.0.EndTime 01:00:00 \
    --Mod.DevTimeSections.0.DayOfWeek 1 \
    --Mod.DevTimeSections.0.StartTime 00:00:00 \
    --Mod.DevTimeSections.0.EndTime 00:30:00 \
    --Mod.Scale 1
```

Output: 
```
{
    "Response": {}
}
```

