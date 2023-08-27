**Example 1: 成功**



Input: 

```
tccli iss DescribeTask --cli-unfold-argument  \
    --TaskId 6d915841-****-****-****-5b278a217051
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "6d915841-****-****-****-5b278a217051",
            "Status": 2,
            "FailReason": "",
            "Progress": 0.94,
            "TaskType": 2,
            "Action": "BatchEnableDevice",
            "ActionZhDesc": "批量启用设备",
            "Total": 3,
            "SuccessCount": 1,
            "FailCount": 1,
            "RunningCount": 1,
            "ResourceId": "",
            "StartedAt": "2023-07-18 12:15:41",
            "CreatedAt": "2023-07-18 12:11:57",
            "UpdatedAt": "2023-07-18 14:27:06",
            "Runtime": 170209866
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

