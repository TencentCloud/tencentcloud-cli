**Example 1: 成功**

 

Input: 

```
tccli iss AddRecordTemplate --cli-unfold-argument  \
    --TemplateName name \
    --TimeSections.0.DayOfWeek 1 \
    --TimeSections.0.StartTime 08:00:00 \
    --TimeSections.0.EndTime 12:00:00 \
    --TimeSections.1.DayOfWeek 1 \
    --TimeSections.1.StartTime 20:30:00 \
    --TimeSections.1.EndTime 23:400:00 \
    --TimeSections.2.DayOfWeek 2 \
    --TimeSections.2.StartTime 12:10:00 \
    --TimeSections.2.EndTime 16:10:00 \
    --TimeSections.3.DayOfWeek 7 \
    --TimeSections.3.StartTime 00:00:00 \
    --TimeSections.3.EndTime 23:59:59
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
                    "DayOfWeek": 1,
                    "StartTime": "08:00:00",
                    "EndTime": "12:00:00"
                },
                {
                    "DayOfWeek": 1,
                    "StartTime": "20:30:00",
                    "EndTime": "23:400:00"
                },
                {
                    "DayOfWeek": 2,
                    "StartTime": "12:10:00",
                    "EndTime": "16:10:00"
                },
                {
                    "DayOfWeek": 7,
                    "StartTime": "00:00:00",
                    "EndTime": "23:59:59"
                }
            ]
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

