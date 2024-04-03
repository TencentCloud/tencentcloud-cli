**Example 1: 修改模板名称**

 

Input: 

```
tccli iss UpdateRecordTemplate --cli-unfold-argument  \
    --TemplateId 48676e89a8c**********baa36220fa4 \
    --Mod.TemplateName newname
```

Output: 
```
{
    "Response": {
        "Data": {
            "TemplateId": "48676e89a8c**********baa36220fa4",
            "TemplateName": "newname",
            "TimeSections": [
                {
                    "DayOfWeek": 3,
                    "StartTime": "10:00:00",
                    "EndTime": "10:30:00"
                }
            ]
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 2: 修改模板上云时间段**

 

Input: 

```
tccli iss UpdateRecordTemplate --cli-unfold-argument  \
    --TemplateId 48676e89a8c**********baa36220fa4 \
    --Mod.TimeSections.0.DayOfWeek 3 \
    --Mod.TimeSections.0.StartTime 10:00:00 \
    --Mod.TimeSections.0.EndTime 10:30:00 \
    --Mod.TimeSections.1.DayOfWeek 4 \
    --Mod.TimeSections.1.StartTime 12:00:00 \
    --Mod.TimeSections.1.EndTime 13:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "TemplateId": "48676e89a8c**********baa36220fa4",
            "TemplateName": "name",
            "TimeSections": [
                {
                    "DayOfWeek": 3,
                    "StartTime": "10:00:00",
                    "EndTime": "10:30:00"
                },
                {
                    "DayOfWeek": 4,
                    "StartTime": "12:00:00",
                    "EndTime": "13:00:00"
                }
            ]
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

