**Example 1: 查询实例列表**



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
        "RequestId": "xx",
        "Items": [
            {
                "WanStatus": 0,
                "Zone": "xx",
                "WanPort": 0,
                "RoVipInfo": {
                    "RoVport": 0,
                    "RoVpcId": 0,
                    "RoVipStatus": 0,
                    "RoVip": "xx",
                    "RoSubnetId": 0
                },
                "Memory": 1000,
                "EngineType": "xx",
                "Status": 1,
                "VpcId": 511512,
                "SlaveInfo": {
                    "Second": {
                        "Vport": 0,
                        "Vip": "xx",
                        "Region": "xx",
                        "Zone": "xx"
                    },
                    "First": {
                        "Vport": 0,
                        "Vip": "xx",
                        "Region": "xx",
                        "Zone": "xx"
                    }
                },
                "InstanceId": "xx",
                "PhysicalId": "xx",
                "Volume": 50,
                "AutoRenew": 0,
                "ProtectMode": 0,
                "CdbError": 0,
                "DeviceClass": "xx",
                "MasterInfo": {
                    "Status": 0,
                    "VpcId": 0,
                    "Zone": "xx",
                    "ExClusterName": "xx",
                    "InstanceId": "xx",
                    "ResourceId": "xx",
                    "Region": "xx",
                    "RegionId": 0,
                    "ZoneId": 0,
                    "Volume": 0,
                    "DeviceType": "xx",
                    "Memory": 0,
                    "SubnetId": 0,
                    "Qps": 0,
                    "TaskStatus": 0,
                    "InstanceName": "xx",
                    "InstanceType": 0,
                    "ExClusterId": "xx"
                },
                "DeployGroupId": "xx",
                "InstanceNodes": 2,
                "RoGroups": [
                    {
                        "RoOfflineDelay": 0,
                        "RoGroupMode": "xx",
                        "RoGroupZone": "xx",
                        "MinRoInGroup": 1,
                        "DelayReplicationTime": 0,
                        "RoGroupId": "xx",
                        "RoMaxDelayTime": 1,
                        "RoGroupName": "xx",
                        "Weight": 0,
                        "UniqVpcId": "xx",
                        "RoInstances": [
                            {
                                "Zone": "xx",
                                "MasterInstanceId": "xx",
                                "Memory": 1000,
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceId": "xx",
                                "Volume": 50,
                                "OfflineTime": "xx",
                                "SubnetId": 115839,
                                "HourFeeStatus": 1,
                                "RoStatus": "xx",
                                "Region": "xx",
                                "DeadlineTime": "xx",
                                "TaskStatus": 0,
                                "DeviceType": "xx",
                                "EngineVersion": "xx",
                                "InstanceName": "xx",
                                "Weight": 0,
                                "PayType": 1,
                                "InstanceType": 3,
                                "Vip": "xx",
                                "Qps": 1000,
                                "Vport": 3306
                            }
                        ],
                        "Vip": "xx",
                        "UniqSubnetId": "xx",
                        "RoGroupRegion": "xx",
                        "Vport": 3306,
                        "WeightMode": "xx"
                    },
                    {
                        "RoOfflineDelay": 0,
                        "RoGroupMode": "xx",
                        "RoGroupZone": "xx",
                        "MinRoInGroup": 1,
                        "DelayReplicationTime": 0,
                        "RoGroupId": "xx",
                        "RoMaxDelayTime": 1,
                        "RoGroupName": "xx",
                        "UniqVpcId": "xx",
                        "Weight": 0,
                        "RoInstances": [
                            {
                                "Zone": "xx",
                                "MasterInstanceId": "xx",
                                "Memory": 1000,
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceId": "xx",
                                "Volume": 25,
                                "OfflineTime": "xx",
                                "SubnetId": 115839,
                                "HourFeeStatus": 1,
                                "RoStatus": "xx",
                                "Region": "xx",
                                "DeadlineTime": "xx",
                                "TaskStatus": 0,
                                "DeviceType": "xx",
                                "EngineVersion": "xx",
                                "InstanceName": "xx",
                                "Weight": 0,
                                "PayType": 1,
                                "InstanceType": 3,
                                "Vip": "xx",
                                "Qps": 1000,
                                "Vport": 3306
                            }
                        ],
                        "Vip": "xx",
                        "UniqSubnetId": "xx",
                        "RoGroupRegion": "xx",
                        "Vport": 3306,
                        "WeightMode": "xx"
                    }
                ],
                "ProjectId": 0,
                "DeadlineTime": "2020-09-22 00:00:00",
                "DeployMode": 0,
                "TaskStatus": 0,
                "SubnetId": 115839,
                "DeviceType": "xx",
                "EngineVersion": "xx",
                "MaxDelayTime": 0,
                "InstanceName": "xx",
                "Cpu": 8,
                "DrInfo": [
                    {
                        "Status": 0,
                        "Zone": "xx",
                        "InstanceId": "xx",
                        "Region": "xx",
                        "SyncStatus": 0,
                        "InstanceName": "xx",
                        "InstanceType": 0
                    }
                ],
                "UniqVpcId": "xx",
                "WanDomain": "xx",
                "InitFlag": 1,
                "PayType": 1,
                "InstanceType": 1,
                "Vip": "xx",
                "UniqSubnetId": "xx",
                "Region": "xx",
                "Qps": 0,
                "Vport": 3306,
                "TagList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "CreateTime": "xx",
                "ZoneId": 720001,
                "ZoneName": "xx"
            }
        ]
    }
}
```

