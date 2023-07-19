**Example 1: 统计任务实例状态**

任务运维-统计任务实例状态

Input: 

```
tccli wedata CountOpsInstanceState --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc
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
        "RequestId": "abc"
    }
}
```

