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
                "DiskType": "test",
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
                        "Vip": "test",
                        "Region": "ap-guangzhou",
                        "Zone": "ap-guangzhou-1"
                    },
                    "First": {
                        "Vport": 0,
                        "Vip": "test",
                        "Region": "ap-guangzhou",
                        "Zone": "ap-guangzhou-1"
                    }
                },
                "InstanceId": "cdn-abc",
                "PhysicalId": "test",
                "Volume": 50,
                "AutoRenew": 0,
                "ProtectMode": 0,
                "CdbError": 0,
                "DeviceClass": "test",
                "MasterInfo": {
                    "Status": 0,
                    "VpcId": 0,
                    "Zone": "100001",
                    "ExClusterName": "test",
                    "InstanceId": "test",
                    "ResourceId": "test",
                    "Region": "ap-guangzhou",
                    "RegionId": 0,
                    "ZoneId": 0,
                    "Volume": 0,
                    "DeviceType": "test",
                    "Memory": 0,
                    "SubnetId": 0,
                    "Qps": 0,
                    "TaskStatus": 0,
                    "InstanceName": "test",
                    "InstanceType": 0,
                    "ExClusterId": "test"
                },
                "DeployGroupId": "test",
                "InstanceNodes": 2,
                "RoGroups": [
                    {
                        "RoOfflineDelay": 0,
                        "RoGroupMode": "test",
                        "RoGroupZone": "test",
                        "MinRoInGroup": 1,
                        "DelayReplicationTime": 0,
                        "RoGroupId": "test",
                        "RoMaxDelayTime": 1,
                        "RoGroupName": "test",
                        "Weight": 0,
                        "UniqVpcId": "test",
                        "RoInstances": [
                            {
                                "Zone": "test",
                                "MasterInstanceId": "test",
                                "Memory": 1000,
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceId": "test",
                                "Volume": 50,
                                "OfflineTime": "test",
                                "SubnetId": 115839,
                                "HourFeeStatus": 1,
                                "RoStatus": "test",
                                "Region": "test",
                                "DeadlineTime": "test",
                                "TaskStatus": 0,
                                "DeviceType": "test",
                                "EngineVersion": "test",
                                "InstanceName": "test",
                                "Weight": 0,
                                "PayType": 1,
                                "InstanceType": 3,
                                "Vip": "test",
                                "Qps": 1000,
                                "Vport": 3306
                            }
                        ],
                        "Vip": "test",
                        "UniqSubnetId": "test",
                        "RoGroupRegion": "test",
                        "Vport": 3306,
                        "WeightMode": "test"
                    },
                    {
                        "RoOfflineDelay": 0,
                        "RoGroupMode": "test",
                        "RoGroupZone": "test",
                        "MinRoInGroup": 1,
                        "DelayReplicationTime": 0,
                        "RoGroupId": "test",
                        "RoMaxDelayTime": 1,
                        "RoGroupName": "test",
                        "UniqVpcId": "test",
                        "Weight": 0,
                        "RoInstances": [
                            {
                                "Zone": "test",
                                "MasterInstanceId": "test",
                                "Memory": 1000,
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceId": "test",
                                "Volume": 25,
                                "OfflineTime": "test",
                                "SubnetId": 115839,
                                "HourFeeStatus": 1,
                                "RoStatus": "test",
                                "Region": "test",
                                "DeadlineTime": "test",
                                "TaskStatus": 0,
                                "DeviceType": "test",
                                "EngineVersion": "test",
                                "InstanceName": "test",
                                "Weight": 0,
                                "PayType": 1,
                                "InstanceType": 3,
                                "Vip": "test",
                                "Qps": 1000,
                                "Vport": 3306
                            }
                        ],
                        "Vip": "test",
                        "UniqSubnetId": "test",
                        "RoGroupRegion": "test",
                        "Vport": 3306,
                        "WeightMode": "test"
                    }
                ],
                "ProjectId": 0,
                "DeadlineTime": "2020-09-22 00:00:00",
                "DeployMode": 0,
                "TaskStatus": 0,
                "SubnetId": 115839,
                "DeviceType": "test",
                "EngineVersion": "test",
                "MaxDelayTime": 0,
                "InstanceName": "test",
                "Cpu": 8,
                "DrInfo": [
                    {
                        "Status": 0,
                        "Zone": "test",
                        "InstanceId": "test",
                        "Region": "test",
                        "SyncStatus": 0,
                        "InstanceName": "test",
                        "InstanceType": 0
                    }
                ],
                "UniqVpcId": "test",
                "WanDomain": "test",
                "InitFlag": 1,
                "PayType": 1,
                "InstanceType": 1,
                "Vip": "test",
                "UniqSubnetId": "test",
                "Region": "test",
                "Qps": 0,
                "Vport": 3306,
                "TagList": [
                    {
                        "TagKey": "test",
                        "TagValue": "test"
                    }
                ],
                "CreateTime": "test",
                "ZoneId": 720001,
                "ZoneName": "test"
            }
        ]
    }
}
```

