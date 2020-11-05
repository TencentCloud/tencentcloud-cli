**Example 1: Registering a migration task**

This example shows you how to register a migration task.

Input: 

```
tccli msp RegisterMigrationTask --cli-unfold-argument  \
    --TaskType database\
    --TaskName ccc\
    --ServiceSupplier TencentCloud\
    --CreateTime '2018-07-13 15:00:00'\
    --UpdateTime '2018-07-13 15:00:00'\
    --MigrateClass mysql:mysql\
    --SrcInfo.Region ap-beijing\
    --SrcInfo.Ip 127.0.0.1\
    --SrcInfo.Port 80\
    --DstInfo.Region ap-beijing\
    --DstInfo.Ip 127.0.0.1\
    --DstInfo.Port 80\
    --SrcAccessType cvm\
    --SrcDatabaseType mysql\
    --DstAccessType cvm\
    --DstDatabaseType mysql
```

Output: 
```
{
    "Response": {
        "TaskId": "msp-jitoh33n",
        "RequestId": "be64a8a3-932f-4ea0-91af-843f537c5648"
    }
}
```

