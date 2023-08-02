**Example 1: 成功**

 

Input: 

```
tccli iss DescribeRecordTemplate --cli-unfold-argument  \
    --TemplateId 48676e89a8c**********baa36220fa4
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
                    "DayOfWeek": 2,
                    "StartTime": "01:00:00",
                    "EndTime": "01:10:00"
                },
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

