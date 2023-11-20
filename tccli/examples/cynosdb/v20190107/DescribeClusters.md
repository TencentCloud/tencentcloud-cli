**Example 1: 查询集群列表**

查询集群列表

Input: 

```
tccli cynosdb DescribeClusters --cli-unfold-argument  \
    --DbType MYSQL \
    --Limit 20 \
    --Filters.0.Values cynosdbpg-ins-bzkxxrmt \
    --Filters.0.Names InstanceId \
    --Filters.0.ExactMatch true \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ClusterSet": [
            {
                "Status": "abc",
                "UpdateTime": "abc",
                "Zone": "abc",
                "ClusterName": "abc",
                "Region": "abc",
                "DbVersion": "abc",
                "ClusterId": "abc",
                "InstanceNum": 0,
                "Uin": "abc",
                "DbType": "abc",
                "AppId": 0,
                "StatusDesc": "abc",
                "CreateTime": "abc",
                "PayMode": 0,
                "PeriodEndTime": "abc",
                "Vip": "abc",
                "Vport": 0,
                "ProjectID": 0,
                "VpcId": "abc",
                "SubnetId": "abc",
                "CynosVersion": "abc",
                "StorageLimit": 0,
                "RenewFlag": 0,
                "ProcessingTask": "abc",
                "Tasks": [
                    {
                        "TaskId": 0,
                        "TaskType": "abc",
                        "TaskStatus": "abc",
                        "ObjectId": "abc",
                        "ObjectType": "abc"
                    }
                ],
                "ResourceTags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "DbMode": "abc",
                "ServerlessStatus": "abc",
                "Storage": 0,
                "StorageId": "abc",
                "StoragePayMode": 0,
                "MinStorageSize": 0,
                "MaxStorageSize": 0,
                "NetAddrs": [
                    {
                        "Vip": "abc",
                        "Vport": 0,
                        "WanDomain": "abc",
                        "WanPort": 0,
                        "NetType": "abc",
                        "UniqSubnetId": "abc",
                        "UniqVpcId": "abc",
                        "Description": "abc",
                        "WanIP": "abc",
                        "WanStatus": "abc",
                        "InstanceGroupId": "abc"
                    }
                ],
                "PhysicalZone": "abc",
                "MasterZone": "abc",
                "HasSlaveZone": "abc",
                "SlaveZones": [
                    "abc"
                ],
                "BusinessType": "abc",
                "IsFreeze": "abc",
                "OrderSource": "abc",
                "Ability": {
                    "IsSupportSlaveZone": "abc",
                    "NonsupportSlaveZoneReason": "abc",
                    "IsSupportRo": "abc",
                    "NonsupportRoReason": "abc"
                },
                "ResourcePackages": [
                    {
                        "PackageId": "abc",
                        "PackageType": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

