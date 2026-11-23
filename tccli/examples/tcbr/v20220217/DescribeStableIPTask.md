**Example 1: 查询固定 IP 任务状态**



Input: 

```
tccli tcbr DescribeStableIPTask --cli-unfold-argument  \
    --EnvId 1 \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a33ae2b6-baf1-4450-a0f4-a319c8698692",
        "Result": "success",
        "TaskId": 7496
    }
}
```

