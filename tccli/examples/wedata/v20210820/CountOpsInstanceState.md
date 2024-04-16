**Example 1: 统计任务实例状态示例**

任务运维-统计任务实例状态

Input: 

```
tccli wedata CountOpsInstanceState --cli-unfold-argument  \
    --TaskId your taskId \
    --ProjectId your projectId
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": 1,
            "Running": 1,
            "Waiting": 1,
            "Depend": 1,
            "Failed": 1,
            "Stopped": 1
        },
        "RequestId": "40za5450-0fa4-49c9-b2f6-66232e84737c"
    }
}
```

