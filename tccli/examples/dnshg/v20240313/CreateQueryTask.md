**Example 1: 添加任务**

添加任务

Input: 

```
tccli dnshg CreateQueryTask --cli-unfold-argument  \
    --TaskType 1 \
    --StartTime 2024-04-01 \
    --EndTime 2024-04-02 \
    --Contents 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "e2f3f70d-834f-4e6d-9e87-26333f00db05",
        "TaskId": "tid-E3kQM2qbbO"
    }
}
```

