**Example 1: 查询实例组（废弃）**

查询实例组网络信息. 该接口已废弃，推荐使用DescribeClusterInstanceGroups

Input: 

```
tccli cynosdb DescribeClusterInstanceGrps --cli-unfold-argument  \
    --ClusterId cynosdbmysql-oib3wx0i
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceGrpInfoList": [
            {
                "AppId": 0,
                "ClusterId": "abc",
                "CreatedTime": "2020-09-22 00:00:00",
                "DeletedTime": "2020-09-22 00:00:00",
                "InstanceGrpId": "abc",
                "Status": "abc",
                "Type": "abc",
                "UpdatedTime": "2020-09-22 00:00:00",
                "Vip": "abc",
                "Vport": 0,
                "WanDomain": "abc",
                "WanIP": "abc",
                "WanPort": 0,
                "WanStatus": "abc",
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
                        "DbMode": "abc",
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
                        ],
                        "ResourcePackages": [
                            {
                                "PackageId": "abc",
                                "PackageType": "abc"
                            }
                        ],
                        "InstanceIndexMode": "abc"
                    }
                ],
                "UniqVpcId": "abc",
                "UniqSubnetId": "abc",
                "OldAddrInfo": {
                    "Vip": "abc",
                    "Vport": 0,
                    "ReturnTime": "abc"
                },
                "ProcessingTasks": [
                    "abc"
                ],
                "Tasks": [
                    {
                        "TaskId": 0,
                        "TaskType": "abc",
                        "TaskStatus": "abc",
                        "ObjectId": "abc",
                        "ObjectType": "abc"
                    }
                ],
                "NetServiceId": 0
            }
        ],
        "InstanceGroupInfoList": [
            {
                "AppId": 0,
                "ClusterId": "abc",
                "CreatedTime": "abc",
                "DeletedTime": "abc",
                "InstanceGroupId": "abc",
                "Status": "abc",
                "Type": "abc",
                "UpdatedTime": "abc",
                "Vip": "abc",
                "Vport": 0,
                "WanDomain": "abc",
                "WanIP": "abc",
                "WanPort": 0,
                "WanStatus": "abc",
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
                        "DbMode": "abc",
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
                        ],
                        "ResourcePackages": [
                            {
                                "PackageId": "abc",
                                "PackageType": "abc"
                            }
                        ],
                        "InstanceIndexMode": "abc"
                    }
                ],
                "UniqVpcId": "abc",
                "UniqSubnetId": "abc",
                "OldAddrInfo": {
                    "Vip": "abc",
                    "Vport": 0,
                    "ReturnTime": "abc"
                },
                "ProcessingTasks": [
                    "abc"
                ],
                "Tasks": [
                    {
                        "TaskId": 0,
                        "TaskType": "abc",
                        "TaskStatus": "abc",
                        "ObjectId": "abc",
                        "ObjectType": "abc"
                    }
                ],
                "NetServiceId": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

