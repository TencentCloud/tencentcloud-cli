**Example 1: 设置实例续费标记**



Input: 

```
tccli sqlserver ModifyDBInstanceRenewFlag --cli-unfold-argument  \
    --RenewFlags.0.InstanceId mssql-j8kv137v \
    --RenewFlags.0.RenewFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "Count": 1
    }
}
```

