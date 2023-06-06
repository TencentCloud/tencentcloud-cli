**Example 1: 查询云数据库异地备份配置信息**

查询云数据库异地备份配置信息

Input: 

```
tccli cdb DescribeRemoteBackupConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv
```

Output: 
```
{
    "Response": {
        "ExpireDays": 7,
        "RemoteBackupSave": "on",
        "RemoteBinlogSave": "on",
        "RemoteRegion": [
            "ap-guangzhou",
            "ap-shanghai"
        ],
        "RegionList": [
            "ap-guangzhou",
            "ap-shanghai",
            "ap-beijing",
            "ap-shanghai"
        ],
        "RequestId": "9d73ec37-89b8-4d36-9f40-123123123"
    }
}
```

