**Example 1: 查询集群列表**



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
        "TotalCount": 597,
        "ClusterSet": [
            {
                "ServerlessStatus": "xx",
                "RenewFlag": 0,
                "Zone": "xx",
                "InstanceNum": 1,
                "ClusterId": "xx",
                "DbVersion": "xx",
                "Storage": 0,
                "StorageId": "xx",
                "ProcessingTask": "xx",
                "Status": "xx",
                "PhysicalZone": "xx",
                "UpdateTime": "xx",
                "VpcId": "xx",
                "Ability": [
                    {
                        "NonsupportSlaveZoneReason": "xx",
                        "IsSupportSlaveZone": "xx",
                        "IsSupportRo": "xx",
                        "NonsupportRoReason": "xx"
                    }
                ],
                "StorageLimit": 30000,
                "SlaveZones": [
                    "xx"
                ],
                "DbMode": "xx",
                "SubnetId": "xx",
                "MinStorageSize": 10,
                "MaxStorageSize": 30000,
                "IsFreeze": "xx",
                "Region": "xx",
                "MasterZone": "xx",
                "PayMode": 1,
                "PeriodEndTime": "xx",
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
                "Tasks": [
                    {
                        "ObjectType": "xx",
                        "TaskStatus": "xx",
                        "ObjectId": "xx",
                        "TaskId": 0,
                        "TaskType": "xx"
                    }
                ],
                "HasSlaveZone": "xx",
                "ClusterName": "xx",
                "ProjectID": 0,
                "Uin": "xx",
                "DbType": "xx",
                "Vip": "xx",
                "AppId": 251007582,
                "OrderSource": "xx",
                "Vport": 3306,
                "CreateTime": "xx",
                "NetAddrs": [
                    {
                        "WanStatus": "xx",
                        "Description": "xx",
                        "UniqVpcId": "xx",
                        "WanDomain": "xx",
                        "WanPort": 0,
                        "Vip": "xx",
                        "UniqSubnetId": "xx",
                        "NetType": "xx",
                        "WanIP": "xx",
                        "Vport": 3306
                    },
                    {
                        "WanStatus": "xx",
                        "Description": "xx",
                        "UniqVpcId": "xx",
                        "WanDomain": "xx",
                        "WanPort": 0,
                        "Vip": "xx",
                        "UniqSubnetId": "xx",
                        "NetType": "xx",
                        "WanIP": "xx",
                        "Vport": 3306
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

