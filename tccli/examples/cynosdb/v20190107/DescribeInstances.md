**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli cynosdb DescribeInstances --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --OrderBy abc \
    --OrderByType abc \
    --Filters.0.Names abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --Filters.0.Name abc \
    --Filters.0.Operator abc \
    --DbType abc \
    --Status abc \
    --InstanceIds abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceSet": [
            {
                "Uin": "abc",
                "AppId": 0,
                "ClusterId": "abc",
                "ClusterName": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "ProjectId": 0,
                "Region": "abc",
                "Zone": "abc",
                "Status": "abc",
                "StatusDesc": "abc",
                "DbType": "abc",
                "DbVersion": "abc",
                "Cpu": 0,
                "Memory": 0,
                "Storage": 0,
                "InstanceType": "abc",
                "InstanceRole": "abc",
                "UpdateTime": "2020-09-22 00:00:00",
                "CreateTime": "2020-09-22 00:00:00",
                "VpcId": "abc",
                "SubnetId": "abc",
                "Vip": "abc",
                "Vport": 0,
                "PayMode": 0,
                "PeriodEndTime": "2020-09-22 00:00:00",
                "DestroyDeadlineText": "abc",
                "IsolateTime": "2020-09-22 00:00:00",
                "NetType": 0,
                "WanDomain": "abc",
                "WanIP": "abc",
                "WanPort": 0,
                "WanStatus": "abc",
                "DestroyTime": "abc",
                "CynosVersion": "abc",
                "ProcessingTask": "abc",
                "RenewFlag": 0,
                "MinCpu": 0,
                "MaxCpu": 0,
                "ServerlessStatus": "abc",
                "StorageId": "abc",
                "StoragePayMode": 0,
                "PhysicalZone": "abc",
                "BusinessType": "abc",
                "Tasks": [
                    {
                        "TaskId": 0,
                        "TaskType": "abc",
                        "TaskStatus": "abc",
                        "ObjectId": "abc",
                        "ObjectType": "abc"
                    }
                ],
                "IsFreeze": "abc",
                "ResourceTags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "MasterZone": "abc",
                "SlaveZones": [
                    "abc"
                ],
                "InstanceNetInfo": [
                    {
                        "InstanceGroupType": "abc",
                        "InstanceGroupId": "abc",
                        "VpcId": "abc",
                        "SubnetId": "abc",
                        "NetType": 0,
                        "Vip": "abc",
                        "Vport": 0,
                        "WanDomain": "abc",
                        "WanIP": "abc",
                        "WanPort": 0,
                        "WanStatus": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

