**Example 1: 1**

1

Input: 

```
tccli cfg DescribeTaskPolicyTriggerLog --cli-unfold-argument  \
    --TaskId 5491 \
    --Page 1 \
    --PageSize 11
```

Output: 
```
{
    "Response": {
        "RequestId": "1bba6839-682a-4123-9728-ec3fc141235b",
        "TriggerLogs": [
            {
                "Content": "触发护栏测试内容-恢复i",
                "CreatTime": "2023-11-14 12:51:33",
                "Name": "触发护栏测试-恢复",
                "TaskId": 5491,
                "TriggerType": 1
            },
            {
                "Content": "触发护栏测试内容",
                "CreatTime": "2023-11-14 12:37:20",
                "Name": "触发护栏测试",
                "TaskId": 5491,
                "TriggerType": 0
            }
        ]
    }
}
```

