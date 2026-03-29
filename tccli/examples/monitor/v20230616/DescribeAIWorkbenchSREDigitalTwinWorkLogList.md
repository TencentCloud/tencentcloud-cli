**Example 1: 成功**



Input: 

```
tccli monitor DescribeAIWorkbenchSREDigitalTwinWorkLogList --cli-unfold-argument  \
    --TwinID 12 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkLogs": [
                {
                    "ID": 3,
                    "CreatedAt": "2025-07-18T20:02:53.248255+08:00",
                    "TwinID": 14,
                    "TaskID": 17,
                    "StartTime": "2025-07-18T20:02:53.247301+08:00",
                    "Status": "failed",
                    "Result": "{\"error\":\"invalid uin\"}",
                    "TaskName": "报告生成1",
                    "TaskType": "custom"
                }
            ],
            "Total": 10
        },
        "JSONStrPaths": [],
        "RequestId": "09c3c111-12b9-477d-8758-98792dcdc8be"
    }
}
```

