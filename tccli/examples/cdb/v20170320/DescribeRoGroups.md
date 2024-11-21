**Example 1: 查询云数据库实例的所有 RO 组的信息**



Input: 

```
tccli cdb DescribeRoGroups --cli-unfold-argument  \
    --InstanceId cdb-93hvfefg
```

Output: 
```
{
    "Response": {
        "RequestId": "5e18a101-e6f5-440c-a9d3-3b30aef256e1",
        "RoGroups": [
            {
                "DelayReplicationTime": 0,
                "MinRoInGroup": 1,
                "RoGroupId": "cdbrg-lsj**ijm",
                "RoGroupMode": "",
                "RoGroupName": "tommy1",
                "RoGroupRegion": "ap-beijing",
                "RoGroupZone": "ap-beijing-6",
                "RoInstances": [
                    {
                        "DeadlineTime": "2024-11-12 16:11:06",
                        "DeviceType": "CUSTOM",
                        "EngineVersion": "8.0",
                        "HourFeeStatus": 1,
                        "InstanceId": "cdbro-lsjh**jm",
                        "InstanceName": "cdb_ro_21**63",
                        "InstanceType": 3,
                        "MasterInstanceId": "cdb-93**fefg",
                        "Memory": 4000,
                        "OfflineTime": "2024-01-25 15:05:59",
                        "PayType": 0,
                        "Qps": 4400,
                        "Region": "ap-beijing",
                        "RoStatus": "online",
                        "Status": 1,
                        "SubnetId": 2738750,
                        "TaskStatus": 0,
                        "Vip": "172.*.32.13",
                        "Volume": 60,
                        "VpcId": 7078258,
                        "Vport": 3306,
                        "Weight": 2,
                        "Zone": "ap-beijing-6"
                    }
                ],
                "RoMaxDelayTime": 10,
                "RoOfflineDelay": 1,
                "UniqSubnetId": "subnet-jp6**13n",
                "UniqVpcId": "vpc-4ko**3u6",
                "Vip": "172.*.64.7",
                "Vport": 3306,
                "Weight": 0,
                "WeightMode": "system"
            }
        ]
    }
}
```

