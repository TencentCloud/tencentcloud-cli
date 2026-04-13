**Example 1: 回档实例**

回档数据库实例到指定时间点

Input: 

```
tccli mongodb RestoreDBInstance --cli-unfold-argument  \
    --InstanceId cmgo-o59c**** \
    --RestoreTime 2026-03-16 17:45:24 \
    --Databases.0.Db testdb \
    --Databases.0.Collections.0.OldCollection users \
    --Databases.0.Collections.0.NewCollection users_bak0316174524
```

Output: 
```
{
    "Response": {
        "FlowId": 100000068,
        "RequestId": "653add02-24bc-4e00-ac03-45078117895b"
    }
}
```

