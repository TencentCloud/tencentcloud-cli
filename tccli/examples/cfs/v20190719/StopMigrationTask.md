**Example 1: 终止迁移任务**

用于终止迁移任务

Input: 

```
tccli cfs StopMigrationTask --cli-unfold-argument  \
    --TaskId cfsmigrate-29de0e87
```

Output: 
```
{
    "Response": {
        "TaskId": "cfsmigrate-29de0e87",
        "Status": 2,
        "RequestId": "eff7c5d9-c8c4-401a-deda-2108d3cc8b76"
    }
}
```

