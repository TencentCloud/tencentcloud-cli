**Example 1: 查询集群详情**



Input: 

```
tccli cynosdb DescribeClusterDetail --cli-unfold-argument  \
    --ClusterId cynosdbpg-5804k48e
```

Output: 
```
{
    "Response": {
        "Detail": {
            "ServerlessStatus": "xx",
            "NetworkStatus": "xx",
            "Zone": "xx",
            "StorageLimit": 0,
            "DbVersion": "xx",
            "Storage": 0,
            "StorageId": "xx",
            "Tasks": [
                {
                    "ObjectType": "xx",
                    "TaskStatus": "xx",
                    "ObjectId": "xx",
                    "TaskId": 0,
                    "TaskType": "xx"
                }
            ],
            "SubnetName": "xx",
            "ProxyStatus": "xx",
            "Status": "xx",
            "PhysicalZone": "xx",
            "MasterZone": "xx",
            "VpcId": "xx",
            "Ability": {
                "NonsupportSlaveZoneReason": "xx",
                "IsSupportSlaveZone": "xx",
                "IsSupportRo": "xx",
                "NonsupportRoReason": "xx"
            },
            "RoAddr": [
                {
                    "IP": "xx",
                    "Port": 0
                }
            ],
            "ClusterId": "xx",
            "SlaveZones": [
                "xx"
            ],
            "VpcName": "xx",
            "PeriodEndTime": "xx",
            "MinStorageSize": 0,
            "MaxStorageSize": 0,
            "Charset": "xx",
            "IsFreeze": "xx",
            "Region": "xx",
            "IsOpenPasswordComplexity": "xx",
            "PayMode": 0,
            "SubnetId": "xx",
            "ResourceTags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "CynosVersion": "xx",
            "StatusDesc": "xx",
            "StoragePayMode": 0,
            "BusinessType": "xx",
            "LogBin": "xx",
            "HasSlaveZone": "xx",
            "ClusterName": "xx",
            "UsedStorage": 129417216,
            "IsSkipTrade": "xx",
            "CreateTime": "xx",
            "DbType": "xx",
            "Vip": "xx",
            "ProjectID": 0,
            "InstanceSet": [
                {
                    "InstanceStatus": "xx",
                    "InstanceCpu": 2,
                    "InstanceId": "xx",
                    "InstanceRole": "xx",
                    "InstanceStatusDesc": "xx",
                    "InstanceMemory": 4,
                    "InstanceStorage": 100,
                    "InstanceName": "xx",
                    "InstanceType": "xx"
                }
            ],
            "Vport": 5432,
            "DbMode": "xx",
            "PitrType": "xx"
        },
        "RequestId": "xx"
    }
}
```

