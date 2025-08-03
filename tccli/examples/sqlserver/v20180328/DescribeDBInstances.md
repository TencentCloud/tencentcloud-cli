**Example 1: 查询实例列表**



Input: 

```
tccli sqlserver DescribeDBInstances --cli-unfold-argument  \
    --Status 2 \
    --SearchKey 172.17.0.12 \
    --VpcId vpc-mknbt351 \
    --Zone ap-guangzhou-3 \
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
                "Architecture": "MULTI",
                "BackupCycle": [
                    1
                ],
                "BackupCycleType": "daily",
                "BackupModel": "master_no_pkg",
                "BackupSaveDays": 7,
                "BackupTime": "00:15:15",
                "Collation": "Chinese_PRC_CI_AS",
                "Cpu": 2,
                "CreateTime": "2024-09-26 20:00:59",
                "CrossBackupEnabled": "disable",
                "CrossBackupSaveDays": 0,
                "CrossRegions": [],
                "DnsPodDomain": "",
                "EndTime": "0000-00-00 00:00:00",
                "HAFlag": "MIRROR",
                "InstanceId": "mssql-25psend9",
                "InstanceNote": "",
                "InstanceType": "cvmMultiHA",
                "IsDrZone": true,
                "IsolateOperator": "",
                "IsolateTime": "0000-00-00 00:00:00",
                "Memory": 4,
                "Model": 7,
                "MultiSlaveZones": [
                    {
                        "DrInstanceId": "mssqldr-phqpv3mz",
                        "SlaveZone": "ap-guangzhou-3",
                        "SlaveZoneName": "广州三区"
                    },
                    {
                        "DrInstanceId": "mssqldr-6fcqb0vd",
                        "SlaveZone": "ap-guangzhou-3",
                        "SlaveZoneName": "广州三区"
                    }
                ],
                "Name": "ac9488be-9cd7-4db9-93f0-d698795833db",
                "PayMode": 0,
                "Pid": 1038028,
                "ProjectId": 0,
                "ROFlag": "",
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "RenewFlag": 0,
                "ResourceTags": null,
                "SlaveZones": {
                    "SlaveZone": "",
                    "SlaveZoneName": ""
                },
                "StartTime": "2024-09-26 20:00:59",
                "Status": 2,
                "Storage": 20,
                "Style": "EXCLUSIVE",
                "SubFlag": "",
                "SubnetId": 2920039,
                "TgwWanVPort": 0,
                "TimeZone": "China Standard Time",
                "Type": "CLOUD_BSSD",
                "Uid": "gamedb.gz1000432.mssql.db",
                "UniqSubnetId": "subnet-1qz3tgim",
                "UniqVpcId": "vpc-idmq8dwn",
                "UpdateTime": "2024-09-26 20:30:29",
                "UsedStorage": 0,
                "Version": "2017",
                "VersionName": "SQL Server 2017 Enterprise",
                "Vip": "172.16.64.6",
                "VpcId": 81006,
                "Vport": 1433,
                "Zone": "ap-guangzhou-6",
                "ZoneId": 100006
            }
        ],
        "RequestId": "eca79e80-7c7a-11ef-95d0-525400853186",
        "TotalCount": 1
    }
}
```

