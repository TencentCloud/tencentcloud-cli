**Example 1: 查询实例列表**



Input: 

```
tccli cynosdb DescribeInstances --cli-unfold-argument  \
    --OrderBy xx \
    --Status xx \
    --DbType xx \
    --OrderByType xx \
    --Filters.0.Values cynosdbmysql-ins-bzkxxrmt \
    --Filters.0.Names xx \
    --Filters.0.ExactMatch True \
    --Filters.0.Name xx \
    --Offset 0 \
    --Limit 0 \
    --InstanceIds xx
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "ServerlessStatus": "xx",
                "WanStatus": "xx",
                "RenewFlag": 2,
                "Zone": "xx",
                "DbVersion": "xx",
                "Storage": 100,
                "StorageId": "xx",
                "Memory": 4,
                "ProcessingTask": "xx",
                "Status": "xx",
                "PhysicalZone": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "VpcId": "xx",
                "MinCpu": 0.0,
                "MaxCpu": 0.0,
                "InstanceId": "xx",
                "ClusterId": "xx",
                "NetType": 0,
                "IsFreeze": "xx",
                "SubnetId": "xx",
                "InstanceType": "xx",
                "DestroyTime": "xx",
                "IsolateTime": "2020-09-22 00:00:00",
                "DestroyDeadlineText": "xx",
                "ProjectId": 0,
                "Region": "xx",
                "PayMode": 1,
                "PeriodEndTime": "2020-09-22 00:00:00",
                "ResourceTags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "CynosVersion": "xx",
                "StatusDesc": "xx",
                "InstanceName": "xx",
                "Cpu": 2,
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
                "WanDomain": "xx",
                "ClusterName": "xx",
                "InstanceRole": "xx",
                "WanPort": 0,
                "Uin": "xx",
                "DbType": "xx",
                "Vip": "xx",
                "AppId": 251007582,
                "WanIP": "xx",
                "Vport": 0,
                "CreateTime": "2020-09-22 00:00:00"
            },
            {
                "ServerlessStatus": "xx",
                "WanStatus": "xx",
                "RenewFlag": 2,
                "Zone": "xx",
                "DbVersion": "xx",
                "Storage": 100,
                "StorageId": "xx",
                "Memory": 8,
                "ProcessingTask": "xx",
                "Status": "xx",
                "PhysicalZone": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "VpcId": "xx",
                "MinCpu": 0.0,
                "MaxCpu": 0.0,
                "InstanceId": "xx",
                "ClusterId": "xx",
                "NetType": 0,
                "ProjectId": 0,
                "SubnetId": "xx",
                "InstanceType": "xx",
                "DestroyTime": "xx",
                "IsolateTime": "2020-09-22 00:00:00",
                "DestroyDeadlineText": "xx",
                "IsFreeze": "xx",
                "Region": "xx",
                "PayMode": 1,
                "PeriodEndTime": "2020-09-22 00:00:00",
                "ResourceTags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "CynosVersion": "xx",
                "StatusDesc": "xx",
                "InstanceName": "xx",
                "Cpu": 4,
                "StoragePayMode": 0,
                "BusinessType": "xx",
                "Tasks": [
                    {
                        "TaskType": "xx",
                        "TaskStatus": "xx",
                        "TaskId": 0,
                        "ObjectId": "xx",
                        "ObjectType": "xx"
                    }
                ],
                "WanDomain": "xx",
                "ClusterName": "xx",
                "InstanceRole": "xx",
                "WanPort": 0,
                "Uin": "xx",
                "DbType": "xx",
                "Vip": "xx",
                "AppId": 251007582,
                "WanIP": "xx",
                "Vport": 0,
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "TotalCount": 26,
        "RequestId": "xx"
    }
}
```

