**Example 1: 查看任务最近执行批次状态**



Input: 

```
tccli tsf DescribeTaskLastStatus --cli-unfold-argument  \
    --TaskId task-qv8kq6m7
```

Output: 
```
{
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
    "Response": {
        "BatchId": "batch-vk8hn123g",
        "State": "SUCCESS"
    }
}
```

