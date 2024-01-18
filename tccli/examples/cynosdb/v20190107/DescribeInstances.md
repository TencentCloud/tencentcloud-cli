**Example 1: 查询实例列表**

查询实例列表

Input: 

```
tccli cynosdb DescribeInstances --cli-unfold-argument  \
    --Limit 0 \
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
    --InstanceIds cynosdbmysql-ins-1asd45qwe
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceSet": [
            {
                "Uin": "1111111",
                "AppId": 0,
                "ClusterId": "cynosdbmysql-asd45qwe",
                "ClusterName": "abc",
                "InstanceId": "cynosdbmysql-ins-asd45qwe",
                "InstanceName": "abc",
                "ProjectId": 0,
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
                "SubnetId": "subnet-123asd",
                "Vip": "192.0.0.0",
                "Vport": 3306,
                "PayMode": 0,
                "PeriodEndTime": "2020-09-22 00:00:00",
                "DestroyDeadlineText": "abc",
                "IsolateTime": "2020-09-22 00:00:00",
                "NetType": 0,
                "WanDomain": "",
                "WanIP": "",
                "WanPort": 0,
                "WanStatus": "",
                "DestroyTime": "",
                "CynosVersion": "2.0.10",
                "ProcessingTask": "",
                "RenewFlag": 0,
                "MinCpu": 0,
                "MaxCpu": 0,
                "ServerlessStatus": "",
                "StorageId": "",
                "StoragePayMode": 0,
                "PhysicalZone": "ap-guangzhou-3",
                "BusinessType": "",
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
                        "TagKey": "abc",
                        "TagValue": "abc"
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
                        "SubnetId": "subnet-12as45",
                        "NetType": 0,
                        "Vip": "192.0.0.0",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": ""
                    }
                ],
                "ResourcePackages": [
                    {
                        "PackageId": "",
                        "PackageType": ""
                    }
                ],
                "InstanceIndexMode": ""
            }
        ],
        "RequestId": "abc"
    }
}
```

