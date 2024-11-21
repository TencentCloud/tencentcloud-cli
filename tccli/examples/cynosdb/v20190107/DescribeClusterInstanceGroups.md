**Example 1: 查询集群实例组信息**



Input: 

```
tccli cynosdb DescribeClusterInstanceGroups --cli-unfold-argument  \
    --ClusterId cynosdbmysql-sgvwu2is
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceGroupInfoList": [
            {
                "AppId": 0,
                "ClusterId": "cynosdbmysql-sgvwu2is",
                "CreatedTime": "2023-03-14 11:25:36",
                "DeletedTime": "2024-04-19 14:33:28",
                "InstanceGroupId": "cynosdbmysql-grp-xb3e8nxd",
                "Status": "deleted",
                "Type": "ha",
                "UpdatedTime": "2024-04-19 14:33:27",
                "Vip": "1.23.4.1",
                "Vport": 3306,
                "WanDomain": "cynosdbmysql-sgvwu2is.wan.domain.com",
                "WanIP": "3.19.7.1",
                "WanPort": 3306,
                "WanStatus": "closed",
                "InstanceSet": [
                    {
                        "Uin": "372386743",
                        "AppId": 2378462378,
                        "ClusterId": "cynosdbmysql-sgvwu2is",
                        "ClusterName": "MyClusterName",
                        "InstanceId": "cynosdbmysql-ins-cbgs2msn",
                        "InstanceName": "MyInstanceName",
                        "ProjectId": 298,
                        "Region": "ap-guangzhou",
                        "Zone": "ap-guangzhou-5",
                        "Status": "deleted",
                        "StatusDesc": "已删除",
                        "DbMode": "NORMAL",
                        "DbType": "MYSQL",
                        "DbVersion": "5.7",
                        "Cpu": 1,
                        "Memory": 2,
                        "Storage": 30,
                        "InstanceType": "rw",
                        "InstanceRole": "master",
                        "UpdateTime": "2020-09-22 00:00:00",
                        "CreateTime": "2020-09-22 00:00:00",
                        "VpcId": "vpc-bxgsh3nx",
                        "SubnetId": "subnet-a4sjf8us",
                        "Vip": "172.1.23.4",
                        "Vport": 3306,
                        "PayMode": 1,
                        "PeriodEndTime": "2020-09-22 00:00:00",
                        "DestroyDeadlineText": "<4 天",
                        "IsolateTime": "2020-09-22 00:00:00",
                        "NetType": 1,
                        "WanDomain": "cynosdbmysql-sgvwu2is.wan.domain.com",
                        "WanIP": "34.1.25.122",
                        "WanPort": 3306,
                        "WanStatus": "isolated",
                        "DestroyTime": "2020-06-12 00:00:00",
                        "CynosVersion": "3.1.10",
                        "ProcessingTask": "taskClosePasswordComplexity",
                        "RenewFlag": 1,
                        "MinCpu": 1,
                        "MaxCpu": 4,
                        "ServerlessStatus": "paused",
                        "StorageId": "cynosdbmysql-sgvwu2is",
                        "StoragePayMode": 1,
                        "PhysicalZone": "ap-guangzhou-5",
                        "BusinessType": "bus_a",
                        "Tasks": [
                            {
                                "TaskId": 34234,
                                "TaskType": "taskCreateCluster",
                                "TaskStatus": "success",
                                "ObjectId": "cynosdbmysql-sgvwu2is",
                                "ObjectType": "taskObjTypeCluster"
                            }
                        ],
                        "IsFreeze": "yes",
                        "ResourceTags": [
                            {
                                "TagKey": "tag_key_1",
                                "TagValue": "tag_value_1"
                            }
                        ],
                        "MasterZone": "ap-guangzhou-5",
                        "SlaveZones": [
                            "ap-guangzhou-7"
                        ],
                        "InstanceNetInfo": [
                            {
                                "InstanceGroupType": "ha",
                                "InstanceGroupId": "cynosdbmysql-grp-sb2u8exh",
                                "VpcId": "vpc-2ysb7hsg",
                                "SubnetId": "subnet-t62sji8s",
                                "NetType": 1,
                                "Vip": "172.3.41.33",
                                "Vport": 3306,
                                "WanDomain": "cynosdbmysql-sgvwu2is.wan.domain.com",
                                "WanIP": "3.1.5.6",
                                "WanPort": 3306,
                                "WanStatus": "isolated"
                            }
                        ],
                        "ResourcePackages": [
                            {
                                "PackageId": "package-xb8sh2js",
                                "PackageType": "CCU",
                                "DeductionPriority": 2
                            }
                        ],
                        "InstanceIndexMode": "mixedRowColumn"
                    }
                ],
                "UniqVpcId": "vpc-2ysb7hsg",
                "UniqSubnetId": "subnet-t62sji8s",
                "OldAddrInfo": {
                    "Vip": "12.4.23.44",
                    "Vport": 3306,
                    "ReturnTime": "2024-01-23 11:23:00"
                },
                "ProcessingTasks": [
                    "taskCloseAudit"
                ],
                "Tasks": [
                    {
                        "TaskId": 234234,
                        "TaskType": "taskCloseAudit",
                        "TaskStatus": "processing",
                        "ObjectId": "cynosdbmysql-sgvwu2is",
                        "ObjectType": "taskObjTypeCluster"
                    }
                ],
                "NetServiceId": 112496
            }
        ],
        "RequestId": "097ecbc0-a5e8-4c30-a4da-5a0faf312d8b"
    }
}
```

