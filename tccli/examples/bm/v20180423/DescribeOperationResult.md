**Example 1: 查询异步任务状态**



Input: 

```
tccli bm DescribeOperationResult --cli-unfold-argument  \
    --TaskId 123
```

Output: 
```
{
    "Response": {
        "TaskStatus": 1,
        "SubtaskStatusSet": [
            {
                "InstanceId": "cpm-xxx",
                "TaskStatus": 1
            }
        ],
        "RequestId": "223956ff-6e06-40a0-9aad-1056627ed72a"
    }
}
```

