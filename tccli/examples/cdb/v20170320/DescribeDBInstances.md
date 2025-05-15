**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli cdb DescribeDBInstances --cli-unfold-argument  \
    --InstanceIds cdb-70zdmgg1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "97939db3-ef94-4a60-9b64-2a1f4e2f1ea3",
        "Items": [
            {
                "WanStatus": 0,
                "Zone": "100001",
                "WanPort": 0,
                "DiskType": "CLOUD_SSD",
                "RoVipInfo": {
                    "RoVport": 0,
                    "RoVpcId": 0,
                    "RoVipStatus": 0,
                    "RoVip": "192.168.1.1",
                    "RoSubnetId": 0
                },
                "Memory": 1000,
                "EngineType": "InnoDB",
                "Status": 1,
                "VpcId": 511512,
                "SlaveInfo": {
                    "Second": {
                        "Vport": 0,
                        "Vip": "172.1.1.1",
                        "Region": "ap-guangzhou",
                        "Zone": "ap-guangzhou-1"
                    },
                    "First": {
                        "Vport": 0,
                        "Vip": "17.1.1.1",
                        "Region": "ap-guangzhou",
                        "Zone": "ap-guangzhou-1"
                    }
                },
                "InstanceId": "cdn-ahend",
                "PhysicalId": "136527",
                "Volume": 50,
                "AutoRenew": 0,
                "ProtectMode": 0,
                "CdbError": 0,
                "DeviceClass": "20",
                "MasterInfo": {
                    "Status": 1,
                    "VpcId": 0,
                    "Zone": "100001",
                    "ExClusterName": "andy",
                    "InstanceId": "cdb-hsyhend",
                    "ResourceId": "",
                    "Region": "ap-guangzhou",
                    "RegionId": 0,
                    "ZoneId": 0,
                    "Volume": 0,
                    "DeviceType": "UNIVERSAL",
                    "Memory": 0,
                    "SubnetId": 0,
                    "Qps": 0,
                    "TaskStatus": 0,
                    "InstanceName": "cdb342",
                    "InstanceType": 0,
                    "ExClusterId": "cdb-3ho6jddd"
                },
                "DeployGroupId": "ps-7t11vrwf",
                "InstanceNodes": 2,
                "RoGroups": [
                    {
                        "RoOfflineDelay": 0,
                        "RoGroupMode": "alone",
                        "RoGroupZone": "800003",
                        "MinRoInGroup": 1,
                        "DelayReplicationTime": 0,
                        "RoGroupId": "cdbrg-92zkeaq2",
                        "RoMaxDelayTime": 1,
                        "RoGroupName": "cdbro2",
                        "Weight": 0,
                        "UniqVpcId": "vpc-ja6ts123",
                        "RoInstances": [
                            {
                                "Zone": "ap-guangzhou-3",
                                "MasterInstanceId": "cdb-fapcrp1q",
                                "ReplicationStatus": "success",
                                "Memory": 1000,
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceId": "cdb-hendhs",
                                "Volume": 50,
                                "OfflineTime": "2024-09-09 16:40:31",
                                "SubnetId": 115839,
                                "HourFeeStatus": 1,
                                "RoStatus": "online",
                                "Region": "ap-guangzhou",
                                "DeadlineTime": "2024-12-29 08:37:33",
                                "TaskStatus": 0,
                                "DeviceType": "UNIVERSAL",
                                "EngineVersion": "5.7",
                                "InstanceName": "cdbro732",
                                "Weight": 0,
                                "PayType": 1,
                                "InstanceType": 3,
                                "Vip": "127.0.0.1",
                                "Qps": 1000,
                                "Vport": 3306
                            }
                        ],
                        "Vip": "10.89.90.66",
                        "UniqSubnetId": "subnet-njh2bc99",
                        "RoGroupRegion": "ap-guangzhou",
                        "Vport": 3306,
                        "WeightMode": "system"
                    },
                    {
                        "RoOfflineDelay": 0,
                        "RoGroupMode": "alone",
                        "RoGroupZone": "ap-guangzhou",
                        "MinRoInGroup": 1,
                        "DelayReplicationTime": 0,
                        "RoGroupId": "cdbrg-92zkeaq4",
                        "RoMaxDelayTime": 1,
                        "RoGroupName": "andy6",
                        "UniqVpcId": "vpc-ja6ts453",
                        "Weight": 0,
                        "RoInstances": [
                            {
                                "Zone": "ap-guangzhou-4",
                                "MasterInstanceId": "cdb-fapcrp12",
                                "ReplicationStatus": "success",
                                "Memory": 1000,
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceId": "cdbro-c1nl9rpv",
                                "Volume": 25,
                                "OfflineTime": "2024-09-09 16:40:30",
                                "SubnetId": 115839,
                                "HourFeeStatus": 1,
                                "RoStatus": "online",
                                "Region": "ap-guangzhou",
                                "DeadlineTime": "2024-12-29 08:37:33",
                                "TaskStatus": 0,
                                "DeviceType": "UNIVERSAL",
                                "EngineVersion": "5.7",
                                "InstanceName": "cdbro7",
                                "Weight": 0,
                                "PayType": 1,
                                "InstanceType": 3,
                                "Vip": "127.0.0.1",
                                "Qps": 1000,
                                "Vport": 3306
                            }
                        ],
                        "Vip": "12.1.1.1",
                        "UniqSubnetId": "subnet-njh2bc11",
                        "RoGroupRegion": "ap-guangzhou",
                        "Vport": 3306,
                        "WeightMode": "system"
                    }
                ],
                "ProjectId": 0,
                "DeadlineTime": "2020-09-22 00:00:00",
                "DeployMode": 0,
                "TaskStatus": 0,
                "SubnetId": 115839,
                "DeviceType": "EXCLUSIVE",
                "EngineVersion": "5.7",
                "MaxDelayTime": 0,
                "InstanceName": "cdbandy",
                "Cpu": 8,
                "DrInfo": [
                    {
                        "Status": 0,
                        "Zone": "ap-beijing-3",
                        "InstanceId": "cdb-hegns",
                        "Region": "ap-beijing",
                        "SyncStatus": 0,
                        "InstanceName": "andydr",
                        "InstanceType": 0
                    }
                ],
                "UniqVpcId": "vpc-5v8wn9m1",
                "WanDomain": "gz-cdb-******.sql.tencentcdb.com",
                "InitFlag": 1,
                "PayType": 1,
                "InstanceType": 1,
                "Vip": "13.1.1.1",
                "UniqSubnetId": "subnet-1typ0s7d",
                "Region": "ap-beijing",
                "Qps": 0,
                "Vport": 3306,
                "TagList": [
                    {
                        "TagKey": "name",
                        "TagValue": "andy"
                    }
                ],
                "CreateTime": "2023-08-29 08:37:33",
                "ZoneId": 720001,
                "ZoneName": "北京三区"
            }
        ]
    }
}
```

