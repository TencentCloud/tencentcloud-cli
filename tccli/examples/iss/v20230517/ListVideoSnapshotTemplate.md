**Example 1: 成功**



Input: 

```
tccli iss ListVideoSnapshotTemplate --cli-unfold-argument  \
    --Sort update_time \
    --Order desc \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "CreateTime": "2026-01-25 12:15:00",
                    "Interval": 3600,
                    "MultiMode": {
                        "Enable": true,
                        "Interval": 180,
                        "Total": 5
                    },
                    "Name": "低频截帧模板",
                    "TemplateId": "035f4**************8*******c1ca5aa4a",
                    "Times": [
                        {
                            "BeginTime": "9:00:00",
                            "EndTime": "12:00:00",
                            "WeekDay": 2
                        }
                    ],
                    "Type": 2,
                    "UpdateTime": "2026-01-25 12:15:00"
                }
            ],
            "Order": "desc",
            "PageNumber": 1,
            "PageSize": 20,
            "Sort": "update_time",
            "TotalCount": 2
        },
        "RequestId": "af39813c-96eb-4c48-b07f-1b31cfe5a9d3"
    }
}
```

