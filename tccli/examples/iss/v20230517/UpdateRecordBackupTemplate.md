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
    "Response": {
        "Data": {
            "CreateAt": "2023-06-02 18:35:35",
            "DevTimeSections": [
                {
                    "DayOfWeek": 1,
                    "EndTime": "00:30:00",
                    "StartTime": "00:00:00"
                }
            ],
            "Scale": 1,
            "TemplateId": "abcdefgh-1234-5678-ijkl-1234567890ab",
            "TemplateName": "test1",
            "TimeSections": [
                {
                    "DayOfWeek": 2,
                    "EndTime": "01:00:00",
                    "StartTime": "00:00:00"
                }
            ],
            "UpdateAt": "2023-06-21 15:03:28"
        },
        "RequestId": "dee0d86a-7821-4519-ba68-e9e846f9e11c"
    }
}
```

