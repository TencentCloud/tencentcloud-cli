**Example 1: 流程ID查询备份详情（备份已完成）**

流程ID查询备份详情（备份已完成）

Input: 

```
tccli sqlserver DescribeBackupByFlowId --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5 \
    --FlowId 1000797
```

Output: 
```
{
    "Response": {
        "BackupName": "mssql-6upluvd5_202007311206",
        "BackupWay": 0,
        "DBs": [
            "db1",
            "db2"
        ],
        "EndTime": "2020-07-31 15:10:27",
        "ExternalAddr": "https://cosback-appid.cos.ap-guangzhou.myqcloud.com/appid%2fsqlserver%2fmssql-mgq355n0%2fbackup%2fautoed_instance_58037_20200728011545.bak.tar?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDpY8YnsLYAbq352rW0KaAnIeqrgJjE0ra%26q-sign-time%3d1596176966%3b1596177266%26q-key-time%3d1596176966%3b1596177266%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3d3ea8139b631fa13d54b2c03313cbf3850d1e0c2c",
        "FileName": "autoed_instance_58037_20200728011545.bak.tar",
        "Id": 1234568,
        "InternalAddr": "https://cosback-appid.cos.ap-guangzhou.myqcloud.com/appid%2fsqlserver%2fmssql-mgq355n0%2fbackup%2fautoed_instance_58037_20200728011545.bak.tar?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDpY8YnsLYAbq352rW0KaAnIeqrgJjE0ra%26q-sign-time%3d1596176966%3b1596177266%26q-key-time%3d1596176966%3b1596177266%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3d3ea8139b631fa13d54b2c03313cbf3850d1e0c2c",
        "RequestId": "3f49f6d4-692b-414b-999c-55b38922e049",
        "Size": 1356532,
        "StartTime": "2020-07-31 14:28:51",
        "Status": 1,
        "Strategy": 0,
        "GroupId": "558800"
    }
}
```

**Example 2: 流程ID查询备份详情（备份创建中）**

流程ID查询备份详情（备份创建中）

Input: 

```
tccli sqlserver DescribeBackupByFlowId --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5 \
    --FlowId 1000796
```

Output: 
```
{
    "Response": {
        "BackupName": "mssql-6upluvd5_202007311206",
        "BackupWay": 0,
        "DBs": [
            "db1",
            "db2"
        ],
        "EndTime": "0000-00-00 00:00:00",
        "ExternalAddr": "",
        "FileName": "",
        "Id": 0,
        "InternalAddr": "",
        "RequestId": "de6cf7f3-ff88-4baf-a933-4714df850efa",
        "Size": 0,
        "StartTime": "2020-07-31 14:27:33",
        "Status": 0,
        "Strategy": 0,
        "GroupId": "558800"
    }
}
```

