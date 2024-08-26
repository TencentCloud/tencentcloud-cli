**Example 1: 使用一台 Linux 在线迁移临时实例**



Input: 

```
tccli lighthouse CreateInstanceForMigrate --cli-unfold-argument  \
    --ClientToken migrate-test-abc \
    --OsType LINUX_UNIX \
    --SystemDisk.DiskSize 30
```

Output: 
```
{
    "Response": {
        "InstanceId": "lhmins-m9oaw2cp",
        "RequestId": "ed584db5-817b-4a88-bb0e-c9112a2be9f8"
    }
}
```

