**Example 1: Querying the list of instances**



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
        "RequestId": "756bb037-a44a-4b4f-abe0-6efd34a6c792",
        "Items": [
            {
                "WanStatus": 0,
                "Zone": "ap-chengdu-1",
                "InitFlag": 1,
                "Memory": 1000,
                "Status": 1,
                "VpcId": 511512,
                "SlaveInfo": {
                    "First": {
                        "Vip": "",
                        "Region": "ap-chengdu",
                        "Vport": 0,
                        "Zone": "ap-chengdu-1"
                    }
                },
                "InstanceId": "cdb-70zdmgg1",
                "Volume": 50,
                "AutoRenew": 0,
                "ProtectMode": 0,
                "RoGroups": [
                    {
                        "RoInstances": [
                            {
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceType": 3,
                                "Zone": "ap-chengdu-1",
                                "Qps": 1000,
                                "InstanceId": "cdbro-3i70uj0k",
                                "Region": "ap-chengdu",
                                "DeadlineTime": "0000-00-00 00:00:00",
                                "PayType": 1,
                                "TaskStatus": 0,
                                "Volume": 50,
                                "EngineVersion": "5.6",
                                "DeviceType": "CUSTOM",
                                "Memory": 1000,
                                "SubnetId": 115839,
                                "Vip": "172.16.0.11",
                                "Vport": 3306,
                                "InstanceName": "cdb_ro_103608",
                                "HourFeeStatus": 1
                            }
                        ],
                        "MinRoInGroup": 1,
                        "Vip": "172.16.0.11",
                        "RoGroupName": "ro_group_103608",
                        "Vport": 3306,
                        "WeightMode": "system",
                        "RoGroupId": "cdbrg-3i70uj0k",
                        "RoMaxDelayTime": 1
                    },
                    {
                        "RoInstances": [
                            {
                                "Status": 1,
                                "VpcId": 511512,
                                "InstanceType": 3,
                                "Zone": "ap-chengdu-1",
                                "Qps": 1000,
                                "InstanceId": "cdbro-6scijza8",
                                "Region": "ap-chengdu",
                                "DeadlineTime": "0000-00-00 00:00:00",
                                "PayType": 1,
                                "TaskStatus": 0,
                                "Volume": 25,
                                "EngineVersion": "5.6",
                                "DeviceType": "CUSTOM",
                                "Memory": 1000,
                                "SubnetId": 115839,
                                "Vip": "172.16.0.25",
                                "Vport": 3306,
                                "InstanceName": "cdb_ro_103610",
                                "HourFeeStatus": 1
                            }
                        ],
                        "MinRoInGroup": 1,
                        "Vip": "172.16.0.25",
                        "RoGroupName": "ro_group_103610",
                        "Vport": 3306,
                        "WeightMode": "system",
                        "RoGroupId": "cdbrg-6scijza8",
                        "RoMaxDelayTime": 1
                    }
                ],
                "SubnetId": 115839,
                "InstanceType": 1,
                "ProjectId": 0,
                "Region": "ap-chengdu",
                "DeadlineTime": "0000-00-00 00:00:00",
                "DeployMode": 0,
                "TaskStatus": 0,
                "DeviceType": "CUSTOM",
                "EngineVersion": "5.6",
                "InstanceName": "jersey_test",
                "DrInfo": [],
                "UniqVpcId": "vpc-5v8wn9mg",
                "WanDomain": "",
                "WanPort": 0,
                "PayType": 1,
                "CreateTime": "2018-05-03 14:53:23",
                "Vip": "172.16.0.16",
                "UniqSubnetId": "subnet-1typ0s7d",
                "Vport": 3306,
                "CdbError": 0
            }
        ]
    }
}
```

