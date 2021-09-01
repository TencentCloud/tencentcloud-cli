**Example 1: 查询异步任务的执行结果**



Input: 

```
tccli ssm DescribeAsyncRequestInfo --cli-unfold-argument  \
    --FlowID 123
```

Output: 
```
{
    "Response": {
        "Description": "task is processing",
        "RequestId": "2609a8fd-4584-4f89-98be-8c7ae1b81ef4",
        "TaskStatus": 0
    }
}
```

