**Example 1: 1**

1

Input: 

```
tccli cfg TriggerPolicy --cli-unfold-argument  \
    --TaskId 5491 \
    --Name 触发护栏测试 \
    --Content 触发护栏测试内容 \
    --TriggerType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1050e4e3-ef1a-4e2f-b100-c68dfd38fc75",
        "Success": true,
        "TaskId": 5491
    }
}
```

