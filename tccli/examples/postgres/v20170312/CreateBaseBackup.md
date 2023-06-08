**Example 1: 创建实例基础备份**

手动创建实例基础备份。

Input: 

```
tccli postgres CreateBaseBackup --cli-unfold-argument  \
    --DBInstanceId postgres-dzg9p3kb
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "BaseBackupId": "443c810b-53c6-5d8c-b6d2-1abbe5794529"
    }
}
```

