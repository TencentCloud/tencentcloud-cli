**Example 1: DescribeLifecycleDataTask**



Input: 

```
tccli cfs DescribeLifecycleDataTask --cli-unfold-argument  \
    --StartTime 2024-11-19 10:15:37 \
    --EndTime 2024-10-19 10:15:37 \
    --TaskId task-c1a2b3f4
```

Output: 
```
{
    "Response": {
        "LifecycleDataTask": [
            {
                "TaskId": "task-c1a2b3f4",
                "TaskStatus": "init",
                "CreationTime": "2024-11-19 10:15:37",
                "Type": "restore"
            }
        ],
        "TotalCount": 1,
        "RequestId": "req-abc"
    }
}
```

