**Example 1: 查询异步任务的执行结果**



Input: 

```
tccli ssm DescribeAsyncRequestInfo --cli-unfold-argument  \
    --FlowID 43414
```

Output: 
```
{
    "Response": {
        "Description": "success",
        "RequestId": "a624794f-4fd3-4e92-b00e-ee46eeb51a0c",
        "TaskStatus": 1
    }
}
```

