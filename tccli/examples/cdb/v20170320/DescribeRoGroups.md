**Example 1: Querying the information of all RO groups of a TencentDB instance**



Input: 

```
tccli cdb DescribeRoGroups --cli-unfold-argument  \
    --InstanceId cdb-eggz8oj5
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "RoGroups": [
            {
                "RoGroupName": "ro_group_172023",
                "RoMaxDelayTime": 1,
                "RoOfflineDelay": 0,
                "RoInstances": [
                    {
                        "Zone": "ap-guangzhou-3",
                        "MasterInstanceId": "cdb-eggz8oj5",
                        "Memory": 2000,
                        "Status": 1,
                        "VpcId": 0,
                        "InstanceId": "cdbro-h9k7cx05",
                        "Volume": 100,
                        "ProtectMode": 0,
                        "ProjectId": 0,
                        "SubnetId": 0,
                        "HourFeeStatus": 1,
                        "RoStatus": "online",
                        "OfflineTime": "0000-00-00 00:00:00",
                        "Region": "ap-guangzhou",
                        "DeadlineTime": "2018-01-04 16:48:30",
                        "DeployMode": 0,
                        "ZoneId": 100003,
                        "DeviceType": "CUSTOM",
                        "EngineVersion": "5.6",
                        "TaskStatus": 1,
                        "InstanceName": "cdb_ro_172023",
                        "Weight": 1,
                        "InitFlag": 1,
                        "PayType": 0,
                        "InstanceType": 3,
                        "Vip": "10.66.199.133",
                        "Qps": 2400,
                        "Vport": 3306,
                        "CdbError": 0
                    }
                ],
                "RoGroupId": "cdbrg-eb2w7dto",
                "Vip": "10.66.199.133",
                "MinRoInGroup": 1,
                "Vport": 3306,
                "WeightMode": "system"
            }
        ]
    }
}
```

