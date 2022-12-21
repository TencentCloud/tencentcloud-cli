**Example 1: 修改云数据库异地备份配置信息**



Input: 

```
tccli cdb ModifyRemoteBackupConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --RemoteBackupSave on \
    --RemoteBinlogSave on \
    --RemoteRegion ap-guangzhou \
    --ExpireDays 7
```

Output: 
```
{
    "Response": {
        "RequestId": "9d73ec37-89b8-4d36-9f40-123123123"
    }
}
```

