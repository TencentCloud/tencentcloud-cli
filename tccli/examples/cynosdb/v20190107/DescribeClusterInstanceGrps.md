**Example 1: 查询实例组**



Input: 

```
tccli cynosdb DescribeClusterInstanceGrps --cli-unfold-argument  \
    --ClusterId cynosdbmysql-oib3wx0i
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceGrpInfoList": [
            {
                "Status": "xx",
                "UpdatedTime": "2020-09-22 00:00:00",
                "Tasks": [
                    {
                        "ObjectType": "xx",
                        "TaskStatus": "xx",
                        "ObjectId": "xx",
                        "TaskId": 0,
                        "TaskType": "xx"
                    }
                ],
                "OldAddrInfo": {
                    "Vip": "xx",
                    "Vport": 0,
                    "ReturnTime": "xx"
                },
                "UniqVpcId": "xx",
                "WanDomain": "xx",
                "InstanceSet": [
                    {
                        "ServerlessStatus": "xx",
                        "WanStatus": "xx",
                        "RenewFlag": 0,
                        "Zone": "xx",
                        "DbVersion": "xx",
                        "Storage": 0,
                        "StorageId": "xx",
                        "Memory": 0,
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
                        "PayMode": 0,
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
                        "Cpu": 0,
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
                        "AppId": 0,
                        "WanIP": "xx",
                        "Vport": 0,
                        "CreateTime": "2020-09-22 00:00:00"
                    }
                ],
                "WanPort": 0,
                "ClusterId": "xx",
                "DeletedTime": "2020-09-22 00:00:00",
                "WanStatus": "xx",
                "CreatedTime": "2020-09-22 00:00:00",
                "Vip": "xx",
                "UniqSubnetId": "xx",
                "InstanceGrpId": "xx",
                "AppId": 0,
                "WanIP": "xx",
                "Vport": 0,
                "Type": "xx",
                "NetServiceId": 0,
                "ProcessingTasks": [
                    "xx"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

