**Example 1: 无实时上云模板**

 

Input: 

```
tccli iss ListRecordTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 2: 有实时上云模板**

 

Input: 

```
tccli iss ListRecordTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TemplateId": "9ee325e9984**********a805c19b4e1",
                "TemplateName": "",
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
            {
                "TemplateId": "48676e89a8c**********baa36220fa4",
                "TemplateName": "",
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
                    }
                ]
            }
        ],
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

