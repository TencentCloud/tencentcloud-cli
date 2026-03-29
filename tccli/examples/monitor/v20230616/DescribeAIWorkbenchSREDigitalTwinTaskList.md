**Example 1: 成功**



Input: 

```
tccli monitor DescribeAIWorkbenchSREDigitalTwinTaskList --cli-unfold-argument  \
    --TwinID 12 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Tasks": [
                {
                    "ID": 15,
                    "CreatedAt": "2025-07-15T12:52:14.257741+08:00",
                    "TwinID": 12,
                    "Name": "告警分析",
                    "TaskType": "custom",
                    "TaskConfig": "{\"uin\":456}"
                }
            ],
            "Total": 10
        },
        "JSONStrPaths": [],
        "RequestId": "efeb4cb7-7180-4436-bfef-b3a4fdb55fd1"
    }
}
```

