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
    "Response": {
        "Data": {
            "CreateAt": "2023-06-21 15:20:35",
            "DevTimeSections": [
                {
                    "DayOfWeek": 3,
                    "EndTime": "01:00:00",
                    "StartTime": "00:00:00"
                }
            ],
            "Scale": 1,
            "TemplateId": "abcdefgh-1234-5678-ijkl-1234567890ab",
            "TemplateName": "123456",
            "TimeSections": [
                {
                    "DayOfWeek": 4,
                    "EndTime": "02:00:00",
                    "StartTime": "00:00:00"
                }
            ],
            "UpdateAt": "2023-06-21 15:20:35"
        },
        "RequestId": "391dfee3-dff2-445a-a8aa-37c9e9b3d185"
    }
}
```

