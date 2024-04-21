**Example 1: 集群信息描述**

集群信息描述

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
            "ClusterId": "abc",
            "ClusterName": "abc",
            "Region": "abc",
            "Zone": "abc",
            "PhysicalZone": "abc",
            "Status": "abc",
            "StatusDesc": "abc",
            "ServerlessStatus": "abc",
            "StorageId": "abc",
            "Storage": 0,
            "MaxStorageSize": 0,
            "MinStorageSize": 0,
            "StoragePayMode": 0,
            "VpcName": "abc",
            "VpcId": "abc",
            "SubnetName": "abc",
            "SubnetId": "abc",
            "Charset": "abc",
            "CreateTime": "abc",
            "DbType": "abc",
            "DbMode": "abc",
            "DbVersion": "abc",
            "StorageLimit": 0,
            "UsedStorage": 0,
            "Vip": "abc",
            "Vport": 0,
            "RoAddr": [
                {
                    "IP": "abc",
                    "Port": 0
                }
            ],
            "Ability": {
                "IsSupportSlaveZone": "abc",
                "NonsupportSlaveZoneReason": "abc",
                "IsSupportRo": "abc",
                "NonsupportRoReason": "abc",
                "IsSupportManualSnapshot": "yes"
            },
            "CynosVersion": "abc",
            "BusinessType": "abc",
            "HasSlaveZone": "abc",
            "IsFreeze": "abc",
            "Tasks": [
                {
                    "TaskId": 0,
                    "TaskType": "abc",
                    "TaskStatus": "abc",
                    "ObjectId": "abc",
                    "ObjectType": "abc"
                }
            ],
            "MasterZone": "abc",
            "SlaveZones": [
                "abc"
            ],
            "InstanceSet": [
                {
                    "InstanceId": "abc",
                    "InstanceName": "abc",
                    "InstanceType": "abc",
                    "InstanceStatus": "abc",
                    "InstanceStatusDesc": "abc",
                    "InstanceCpu": 0,
                    "InstanceMemory": 0,
                    "InstanceStorage": 0,
                    "InstanceRole": "abc",
                    "MaintainStartTime": 0,
                    "MaintainDuration": 0,
                    "MaintainWeekDays": [
                        "abc"
                    ],
                    "ServerlessStatus": "abc"
                }
            ],
            "PayMode": 0,
            "PeriodEndTime": "abc",
            "ProjectID": 0,
            "ResourceTags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "ProxyStatus": "abc",
            "LogBin": "abc",
            "IsSkipTrade": "abc",
            "PitrType": "abc",
            "IsOpenPasswordComplexity": "abc",
            "NetworkStatus": "abc",
            "ResourcePackages": [
                {
                    "PackageId": "abc",
                    "PackageType": "abc"
                }
            ],
            "RenewFlag": 0,
            "NetworkType": "abc",
            "SlaveZoneAttr": [
                {
                    "Zone": "ap-guangzhou-5",
                    "BinlogSyncWay": "async"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

