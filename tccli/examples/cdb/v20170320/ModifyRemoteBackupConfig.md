**Example 1: 修改云数据库异地备份配置信息**

无

Input: 

```
tccli cdb ModifyRemoteBackupConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --RemoteBinlogSave on \
    --ExpireDays 7 \
    --RemoteRegion ap-guangzhou \
    --RemoteBackupSave on
```

Output: 
```
{
    "Response": {
        "RequestId": "9d73ec37-89b8-4d36-9f40-123123123"
    }
}
```

