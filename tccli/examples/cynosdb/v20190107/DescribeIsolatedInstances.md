**Example 1: 查询回收站实例列表**



Input: 

```
tccli cynosdb DescribeIsolatedInstances --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --Filters.0.Names InstanceId \
    --Filters.0.Values cynosdbpg-ins-bzkxxrmt \
    --DbType MYSQL
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AppId": 1311111346,
                "BusinessType": "",
                "ClusterId": "cynosdbmysql-grhvkwd",
                "ClusterName": "cynosdbmysql-grhvkwd",
                "Cpu": 2,
                "CreateTime": "2024-12-03 14:03:58",
                "CynosVersion": "2.1.13.001",
                "DbMode": "NORMAL",
                "DbType": "MYSQL",
                "DbVersion": "5.7",
                "DestroyDeadlineText": "<7 天",
                "DestroyTime": "2024-12-30 19:51:33",
                "DeviceType": "exclusive",
                "InstanceAbility": {
                    "IsSupportForceRestart": "no",
                    "NonsupportForceRestartReason": "NoForcedRestartAllowed"
                },
                "InstanceId": "cynosdbmysql-ins-crl6j3l",
                "InstanceIndexMode": "onlyRowIndex",
                "InstanceName": "cynosdbmysql-ins-crl6j3l",
                "InstanceNetInfo": [
                    {
                        "InstanceGroupId": "cynosdbmysql-grp-r7hmdx4",
                        "InstanceGroupType": "ha",
                        "NetType": 1,
                        "SubnetId": "subnet-oiz56c8",
                        "Vip": "172.0.0.2",
                        "VpcId": "vpc-gy34uq2",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": "init"
                    }
                ],
                "InstanceRole": "master",
                "InstanceStorageType": "",
                "InstanceType": "rw",
                "IsFreeze": "no",
                "IsolateTime": "2024-12-23 19:51:33",
                "MasterZone": "ap-chongqing-1",
                "MaxCpu": 0,
                "Memory": 4,
                "MinCpu": 0,
                "NetType": 1,
                "PayMode": 1,
                "PeriodEndTime": "2024-12-23 19:51:24",
                "PhysicalZone": "ap-chongqing-1",
                "ProcessingTask": "",
                "ProjectId": 0,
                "Region": "ap-chongqing",
                "RenewFlag": 1,
                "ResourcePackages": null,
                "ResourceTags": null,
                "ServerlessStatus": "",
                "SlaveZones": [],
                "Status": "isolated",
                "StatusDesc": "已隔离",
                "Storage": 10,
                "StorageId": "cynosdbmysql-grhvkwd",
                "StoragePayMode": 1,
                "SubnetId": "subnet-oiz56c8",
                "Tasks": [],
                "Uin": "100011147054",
                "UpdateTime": "2024-12-23 19:51:33",
                "Vip": "172.0.0.2",
                "VpcId": "vpc-gy34uq2",
                "Vport": 3306,
                "WanDomain": "",
                "WanIP": "",
                "WanPort": 0,
                "WanStatus": "init",
                "Zone": "ap-chongqing-1"
            },
            {
                "AppId": 1311111346,
                "BusinessType": "",
                "ClusterId": "cynosdbmysql-grhvkwd",
                "ClusterName": "cynosdbmysql-grhvkwd",
                "Cpu": 2,
                "CreateTime": "2024-12-03 14:03:58",
                "CynosVersion": "2.1.13.001",
                "DbMode": "NORMAL",
                "DbType": "MYSQL",
                "DbVersion": "5.7",
                "DestroyDeadlineText": "<7 天",
                "DestroyTime": "2024-12-30 19:51:33",
                "DeviceType": "exclusive",
                "InstanceAbility": {
                    "IsSupportForceRestart": "no",
                    "NonsupportForceRestartReason": "NoForcedRestartAllowed"
                },
                "InstanceId": "cynosdbmysql-ins-6t9ynb7",
                "InstanceIndexMode": "onlyRowIndex",
                "InstanceName": "cynosdbmysql-ins-6t9ynb7",
                "InstanceNetInfo": [
                    {
                        "InstanceGroupId": "cynosdbmysql-grp-08o6vj0",
                        "InstanceGroupType": "singleRo",
                        "NetType": 1,
                        "SubnetId": "subnet-oiz56c8",
                        "Vip": "172.0.0.7",
                        "VpcId": "vpc-gy34uq2",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": "init"
                    }
                ],
                "InstanceRole": "ro",
                "InstanceStorageType": "",
                "InstanceType": "ro",
                "IsFreeze": "no",
                "IsolateTime": "2024-12-23 19:51:33",
                "MasterZone": "ap-chongqing-1",
                "MaxCpu": 0,
                "Memory": 4,
                "MinCpu": 0,
                "NetType": 1,
                "PayMode": 1,
                "PeriodEndTime": "2024-12-23 19:51:24",
                "PhysicalZone": "ap-chongqing-1",
                "ProcessingTask": "",
                "ProjectId": 0,
                "Region": "ap-chongqing",
                "RenewFlag": 1,
                "ResourcePackages": null,
                "ResourceTags": null,
                "ServerlessStatus": "",
                "SlaveZones": [],
                "Status": "isolated",
                "StatusDesc": "已隔离",
                "Storage": 10,
                "StorageId": "cynosdbmysql-grhvkwd",
                "StoragePayMode": 1,
                "SubnetId": "subnet-oiz56c8",
                "Tasks": [],
                "Uin": "100011147054",
                "UpdateTime": "2024-12-23 19:51:33",
                "Vip": "172.0.0.7",
                "VpcId": "vpc-gy34uq2",
                "Vport": 3306,
                "WanDomain": "",
                "WanIP": "",
                "WanPort": 0,
                "WanStatus": "init",
                "Zone": "ap-chongqing-1"
            }
        ],
        "RequestId": "8f291dbc-3840-40f9-aa39-841437c247fb",
        "TotalCount": 2
    }
}
```

