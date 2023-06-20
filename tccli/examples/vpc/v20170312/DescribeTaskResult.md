**Example 1: 查询异步任务执行结果**

查询异步任务执行结果。

Input: 

```
tccli vpc DescribeTaskResult --cli-unfold-argument  \
    --TaskId 12566700
```

Output: 
```
{
    "Response": {
        "TaskId": 12566700,
        "Result": "SUCCESS",
        "RequestId": "f2e74569-c189-4396-80ab-1482134a1e52"
    }
}
```

