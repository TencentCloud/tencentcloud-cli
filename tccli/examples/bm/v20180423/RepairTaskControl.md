**Example 1: 维修任务管理-授权维修**



Input: 

```
tccli bm RepairTaskControl --cli-unfold-argument  \
    --TaskId bm-repair-4zywlogv \
    --Operate AuthorizeRepair
```

Output: 
```
{
    "Response": {
        "RequestId": "0436564c-1284-4f0f-a341-59e86f548446",
        "TaskId": 123
    }
}
```

