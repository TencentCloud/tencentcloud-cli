**Example 1: 发起切换任务**

发起切换任务

Input: 

```
tccli cynosdb SwitchFromCDB --cli-unfold-argument  \
    --MigrateDBTaskId 123
```

Output: 
```
{
    "Response": {
        "FlowId": 123,
        "RequestId": "xx"
    }
}
```

