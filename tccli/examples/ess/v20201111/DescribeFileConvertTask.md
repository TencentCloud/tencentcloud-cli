**Example 1: 通过转换任务Id查询任务状态**

通过转换任务Id查询任务状态

Input: 

```
tccli ess DescribeFileConvertTask --cli-unfold-argument  \
    --TaskId 2026070*******692601 \
    --Operator.UserId yDtT9UUckp9***********RvxYJ7r7py
```

Output: 
```
{
    "Response": {
        "ResourceId": "yD3JmUUckpe***********MEcwFQDTq0",
        "TaskId": "2026070*******692601",
        "TaskMessage": "任务处理完成",
        "TaskStatus": 8,
        "RequestId": "751ff83b-8f49-4684-bd80-f596b48ff3e5"
    }
}
```

