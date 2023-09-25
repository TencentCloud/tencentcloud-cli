**Example 1: 查询实例列表**



Input: 

```
tccli sqlserver DescribeDBInstances --cli-unfold-argument  \
    --Status 2 \
    --SearchKey 172.17.0.12 \
    --VpcId vpc-mknbt351 \
    --Zone ap-guangzhou-2 \
    --VersionSet 2008R2 \
    --ProjectId 0 \
    --Offset 0 \
    --PayMode 1 \
    --Limit 3 \
    --InstanceIdSet mssql-3l3fgqn7 \
    --SubnetId subnet-f72hylo6 \
    --TagKeys 测试tag \
    --VipSet 172.1.0.12 \
    --InstanceNameSet 数仓
```

Output: 
```
{
    "Response": {
        "DBInstances": [
            {
                "BackupCycle": [
                    1
                ],
                "BackupCycleType": "daily",
                "BackupModel": "master_pkg",
                "BackupSaveDays": 7,
                "BackupTime": "07:03:00",
                "Collation": "Chinese_PRC_CI_AS",
                "Cpu": 4,
                "CreateTime": "2022-11-07 16:21:01",
                "CrossBackupEnabled": "disable",
                "CrossBackupSaveDays": 0,
                "CrossRegions": [],
                "DnsPodDomain": "",
                "EndTime": "0000-00-00 00:00:00",
                "HAFlag": "SINGLE",
                "InstanceId": "mssql-fz80u7u1",
                "InstanceNote": "",
                "InstanceType": "SI",
                "IsolateOperator": "",
                "IsolateTime": "0000-00-00 00:00:00",
                "Memory": 8,
                "Model": 2,
                "Name": "2008-2012-2016",
                "PayMode": 0,
                "Pid": 1003456,
                "ProjectId": 0,
                "ROFlag": "",
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "RenewFlag": 0,
                "ResourceTags": null,
                "IsDrZone": false,
                "SlaveZones": {
                    "SlaveZone": "",
                    "SlaveZoneName": ""
                },
                "StartTime": "2022-11-07 16:21:01",
                "Status": 2,
                "Storage": 40,
                "SubFlag": "",
                "SubnetId": 2118677,
                "TgwWanVPort": 0,
                "TimeZone": "China Standard Time",
                "Type": "CLOUD_PREMIUM",
                "Uid": "gamedb.gz1208.cdb.db",
                "UniqSubnetId": "subnet-ieianm0o",
                "UniqVpcId": "vpc-o739nubl",
                "UpdateTime": "2022-11-07 20:04:03",
                "UsedStorage": 0,
                "Version": "2019",
                "VersionName": "SQL Server 2019 Enterprise",
                "Vip": "10.24.12.28",
                "VpcId": 5350471,
                "Vport": 1433,
                "Zone": "ap-guangzhou-3",
                "ZoneId": 100003,
                "Architecture": "SINGLE",
                "Style": "SHARED"
            }
        ],
        "RequestId": "de641788-0565-4617-a7f4-639de128772b",
        "TotalCount": 1
    }
}
```

