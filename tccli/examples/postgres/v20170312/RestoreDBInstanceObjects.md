**Example 1: 指定恢复时间，恢复数据库对象**

在原实例上指定恢复时间，恢复某些数据库相关对象。例如在postgres-abcd1234实例上，恢复时间点2024-03-25 01:27:35上的test数据库。

Input: 

```
tccli postgres RestoreDBInstanceObjects --cli-unfold-argument  \
    --DBInstanceId postgres-abcd1234 \
    --RestoreTargetTime 2024-03-25 01:27:35 \
    --RestoreObjects test
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90"
    }
}
```

**Example 2: 选定备份集，恢复数据库对象**

在原实例上选定备份集，恢复某些数据库相关对象。例如在postgres-abcd1234实例上，使用备份集28aa61ac-1b1f-566a-bedb-6e918024be02恢复test数据库。

Input: 

```
tccli postgres RestoreDBInstanceObjects --cli-unfold-argument  \
    --DBInstanceId postgres-abcd1234 \
    --BackupSetId 28aa61ac-1b1f-566a-bedb-6e918024be02 \
    --RestoreObjects test
```

Output: 
```
{
    "Response": {
        "RequestId": "3d49f48c-7d27-4820-8724-ed5b15787373"
    }
}
```

