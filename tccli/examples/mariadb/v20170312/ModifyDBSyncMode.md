**Example 1: 修改云数据库实例的同步模式**



Input: 

```
tccli mariadb ModifyDBSyncMode --cli-unfold-argument  \
    --InstanceId tdsql-avw0207d \
    --SyncMode 0
```

Output: 
```
{
    "Response": {
        "RequestId": "901bd41c-08a2-4001-8364-5a63f32056ae",
        "FlowId": 3521
    }
}
```

