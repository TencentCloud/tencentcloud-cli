**Example 1: 查询实例组（废弃）**

查询实例组网络信息. 该接口已废弃，推荐使用DescribeClusterInstanceGroups

Input: 

```
tccli cynosdb DescribeClusterInstanceGrps --cli-unfold-argument  \
    --ClusterId cynosdbmysql-grhvkwd
```

Output: 
```
{
    "Response": {
        "InstanceGroupInfoList": [
            {
                "AppId": 1312008346,
                "ClusterId": "cynosdbmysql-grhvkwd",
                "CreatedTime": "2024-12-03 14:03:58",
                "DeletedTime": "0001-01-01 00:00:00",
                "InstanceGroupId": "cynosdbmysql-grp-r7hmdx4",
                "InstanceSet": [
                    {
                        "AppId": 1312008346,
                        "BusinessType": "",
                        "ClusterId": "cynosdbmysql-grhvkwd",
                        "ClusterName": "cynosdbmysql-grhvkwd",
                        "Cpu": 2,
                        "CreateTime": "2024-12-03 14:03:58",
                        "CynosVersion": "2.1.13.001",
                        "DbMode": "NORMAL",
                        "DbType": "MYSQL",
                        "DbVersion": "5.7",
                        "DestroyDeadlineText": "",
                        "DestroyTime": "",
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
                        "IsolateTime": "0001-01-01 00:00:00",
                        "MasterZone": "ap-chongqing-1",
                        "MaxCpu": 0,
                        "Memory": 4,
                        "MinCpu": 0,
                        "NetType": 1,
                        "PayMode": 1,
                        "PeriodEndTime": "2025-01-03 14:04:40",
                        "PhysicalZone": "ap-chongqing-1",
                        "ProcessingTask": "",
                        "ProjectId": 0,
                        "Region": "ap-chongqing",
                        "RenewFlag": 1,
                        "ResourcePackages": null,
                        "ResourceTags": null,
                        "ServerlessStatus": "",
                        "SlaveZones": [],
                        "Status": "running",
                        "StatusDesc": "运行中",
                        "Storage": 10,
                        "StorageId": "cynosdbmysql-grhvkwd",
                        "StoragePayMode": 1,
                        "SubnetId": "subnet-oiz56c8",
                        "Tasks": [],
                        "Uin": "100021117054",
                        "UpdateTime": "2024-12-03 14:04:40",
                        "Vip": "172.0.0.12",
                        "VpcId": "vpc-gy34uq2",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": "init",
                        "Zone": "ap-chongqing-1"
                    }
                ],
                "NetServiceId": 53990,
                "OldAddrInfo": {
                    "ReturnTime": "",
                    "Vip": "",
                    "Vport": 0
                },
                "ProcessingTasks": [],
                "Status": "running",
                "Tasks": [],
                "Type": "ha",
                "UniqSubnetId": "subnet-oiz56c8",
                "UniqVpcId": "vpc-gy34uq2",
                "UpdatedTime": "2024-12-03 14:04:40",
                "Vip": "172.0.0.12",
                "Vport": 3306,
                "WanDomain": "",
                "WanIP": "",
                "WanPort": 0,
                "WanStatus": "init"
            },
            {
                "AppId": 1310008346,
                "ClusterId": "cynosdbmysql-grhvkwd",
                "CreatedTime": "2024-12-03 14:03:58",
                "DeletedTime": "0001-01-01 00:00:00",
                "InstanceGroupId": "cynosdbmysql-grp-08o6vjh",
                "InstanceSet": [
                    {
                        "AppId": 1310008346,
                        "BusinessType": "",
                        "ClusterId": "cynosdbmysql-grhvkwd",
                        "ClusterName": "cynosdbmysql-grhvkwd",
                        "Cpu": 2,
                        "CreateTime": "2024-12-03 14:03:58",
                        "CynosVersion": "2.1.13.001",
                        "DbMode": "NORMAL",
                        "DbType": "MYSQL",
                        "DbVersion": "5.7",
                        "DestroyDeadlineText": "",
                        "DestroyTime": "",
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
                        "IsolateTime": "0001-01-01 00:00:00",
                        "MasterZone": "ap-chongqing-1",
                        "MaxCpu": 0,
                        "Memory": 4,
                        "MinCpu": 0,
                        "NetType": 1,
                        "PayMode": 1,
                        "PeriodEndTime": "2025-01-03 14:04:40",
                        "PhysicalZone": "ap-chongqing-1",
                        "ProcessingTask": "",
                        "ProjectId": 0,
                        "Region": "ap-chongqing",
                        "RenewFlag": 1,
                        "ResourcePackages": null,
                        "ResourceTags": null,
                        "ServerlessStatus": "",
                        "SlaveZones": [],
                        "Status": "running",
                        "StatusDesc": "运行中",
                        "Storage": 10,
                        "StorageId": "cynosdbmysql-grhvkwd",
                        "StoragePayMode": 1,
                        "SubnetId": "subnet-oiz56c8",
                        "Tasks": [],
                        "Uin": "100021117054",
                        "UpdateTime": "2024-12-09 15:18:23",
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
                "NetServiceId": 53991,
                "OldAddrInfo": {
                    "ReturnTime": "",
                    "Vip": "",
                    "Vport": 0
                },
                "ProcessingTasks": [],
                "Status": "running",
                "Tasks": [],
                "Type": "singleRo",
                "UniqSubnetId": "subnet-oiz56c8",
                "UniqVpcId": "vpc-gy34uq2",
                "UpdatedTime": "2024-12-03 14:04:40",
                "Vip": "172.0.0.7",
                "Vport": 3306,
                "WanDomain": "",
                "WanIP": "",
                "WanPort": 0,
                "WanStatus": "init"
            }
        ],
        "RequestId": "c32019ab-0d57-4b3d-80ea-5f52c12b523f",
        "TotalCount": 2
    }
}
```

