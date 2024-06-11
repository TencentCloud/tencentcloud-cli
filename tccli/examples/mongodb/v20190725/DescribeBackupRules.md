**Example 1: 查询实例的自动备份规则信息**

查询实例的自动备份规则信息

Input: 

```
tccli mongodb DescribeBackupRules --cli-unfold-argument  \
    --InstanceId cmgo-9d0p****
```

Output: 
```
{
    "Response": {
        "BackupMethod": 0,
        "BackupSaveTime": 7,
        "BackupTime": 1,
        "RequestId": "07ec4290-d682-11ed-aa06-f56fb86dae78"
    }
}
```

