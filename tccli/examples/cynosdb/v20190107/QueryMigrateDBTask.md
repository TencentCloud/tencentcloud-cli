**Example 1: 查询迁移任务**

查询迁移任务

Input: 

```
tccli cynosdb QueryMigrateDBTask --cli-unfold-argument  \
    --MigrateDBTaskId 123
```

Output: 
```
{
    "Response": {
        "DstInstanceInfo": {
            "InstanceId": "",
            "ReadOnlyStatus": "",
            "Vip": "",
            "Vport": 0,
            "WanDomain": "",
            "WanPort": 0
        },
        "ExpireTime": "",
        "MigrateDBTaskId": 0,
        "MigrateTaskStatus": "init",
        "RequestId": "b73db580-a6cb-11ed-b2ab-0524d54048a6",
        "SrcInstanceInfo": {
            "InstanceId": "",
            "ReadOnlyStatus": "",
            "Vip": "",
            "Vport": 0,
            "WanDomain": "",
            "WanPort": 0
        }
    }
}
```

