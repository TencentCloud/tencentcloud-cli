**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli cynosdb DescribeInstances --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --OrderBy CREATETIME \
    --OrderByType ASC \
    --Filters.0.Names status \
    --Filters.0.Values running \
    --Filters.0.ExactMatch True \
    --Filters.0.Name  \
    --Filters.0.Operator  \
    --DbType MYSQL \
    --Status running \
    --InstanceIds cynosdbmysql-ins-1asd5qwe
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceSet": [
            {
                "Uin": "238762734",
                "AppId": 23762834,
                "ClusterId": "cynosdbmysql-asd45qwe",
                "ClusterName": "MyClusterName",
                "InstanceId": "cynosdbmysql-ins-asd45qwe",
                "InstanceName": "MyInstanceName",
                "ProjectId": 2342,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "Status": "running",
                "StatusDesc": "运行中",
                "DbMode": "NORMAL",
                "DbType": "MYSQL",
                "DbVersion": "5.7",
                "Cpu": 1,
                "Memory": 1,
                "Storage": 10,
                "InstanceType": "rw",
                "InstanceRole": "master",
                "UpdateTime": "2020-09-22 00:00:00",
                "CreateTime": "2020-09-22 00:00:00",
                "VpcId": "vpc-12as56",
                "SubnetId": "subnet-12kasd",
                "Vip": "192.0.2.1",
                "Vport": 3306,
                "PayMode": 0,
                "PeriodEndTime": "2020-09-22 00:00:00",
                "DestroyDeadlineText": "<5 天",
                "IsolateTime": "2020-09-22 00:00:00",
                "NetType": 1,
                "WanDomain": "cynosdbpg-bzkxxrmt.wan.domain.com",
                "WanIP": "3.1.5.2",
                "WanPort": 3306,
                "WanStatus": "running",
                "DestroyTime": "2024-01-04 00:09:10",
                "CynosVersion": "2.0.10",
                "ProcessingTask": "taskUpgradeStorage",
                "RenewFlag": 0,
                "MinCpu": 1,
                "MaxCpu": 8,
                "ServerlessStatus": "paused",
                "StorageId": "cynosdbpg-bzkxxrmt",
                "StoragePayMode": 0,
                "PhysicalZone": "ap-guangzhou-3",
                "BusinessType": "bus_a",
                "Tasks": [
                    {
                        "TaskId": 111110,
                        "TaskType": "taskCreateClusters",
                        "TaskStatus": "running",
                        "ObjectId": "cynosdbmysql-asd45qwe",
                        "ObjectType": "cluster"
                    }
                ],
                "IsFreeze": "no",
                "ResourceTags": [
                    {
                        "TagKey": "tag_key_1",
                        "TagValue": "tag_value_1"
                    }
                ],
                "MasterZone": "ap-guangzhou-3",
                "SlaveZones": [
                    "ap-guangzhou-4"
                ],
                "InstanceNetInfo": [
                    {
                        "InstanceGroupType": "ha",
                        "InstanceGroupId": "cynosdbmysql-grp-asd45qwe",
                        "VpcId": "vpc-12as45",
                        "SubnetId": "subnet-cbhs7ush",
                        "NetType": 1,
                        "Vip": "192.0.0.0",
                        "Vport": 3306,
                        "WanDomain": "cynosdbpg-bzkxxrmt.wan,domain,com",
                        "WanIP": "23.15.5.1",
                        "WanPort": 3306,
                        "WanStatus": "running"
                    }
                ],
                "ResourcePackages": [
                    {
                        "DeductionPriority": 0,
                        "PackageId": "package-bhsy2snc",
                        "PackageType": "CCU"
                    }
                ],
                "InstanceIndexMode": "onlyRowIndex"
            }
        ],
        "RequestId": "fd5759b5-89e9-483c-b79c-d99b27c33192"
    }
}
```

