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
            "ClusterId": "cynosdbmysql-abcd1243",
            "ClusterName": "cynodbmysql-自定义用户名",
            "Region": "ap-guangzhou",
            "Zone": "ap-guangzhou-1",
            "PhysicalZone": "ap-guangzhou-1",
            "Status": "running",
            "StatusDesc": "运行中",
            "ServerlessStatus": "运行中",
            "StorageId": "cynosdbmysql-1234abcd",
            "Storage": 20,
            "MaxStorageSize": 1000,
            "MinStorageSize": 10,
            "StoragePayMode": 0,
            "VpcName": "vpc-abcd1234",
            "VpcId": "vpc-abcd1234",
            "SubnetName": "subnet-1234abcd",
            "SubnetId": "subnet-1234abcd",
            "Charset": "utf8mb4",
            "CreateTime": "2020-02-20 20:20:20",
            "DbType": "MYSQL",
            "DbMode": "normal",
            "DbVersion": "5.7",
            "StorageLimit": 20,
            "UsedStorage": 14,
            "Vip": "1.2.3.4",
            "Vport": 3306,
            "RoAddr": [
                {
                    "IP": "1.2.3.5",
                    "Port": 3306
                }
            ],
            "Ability": {
                "IsSupportSlaveZone": "yes",
                "NonsupportSlaveZoneReason": "aaabbbccc",
                "IsSupportRo": "yes",
                "NonsupportRoReason": "aaabbbccc",
                "IsSupportManualSnapshot": "yes"
            },
            "CynosVersion": "3.1.10",
            "BusinessType": "",
            "HasSlaveZone": "",
            "IsFreeze": "no",
            "Tasks": [
                {
                    "TaskId": 10,
                    "TaskType": "taskAutoBackup",
                    "TaskStatus": "processing",
                    "ObjectId": "cynosdbmysql-abcd1234",
                    "ObjectType": "taskObjTypeCluster"
                }
            ],
            "MasterZone": "ap-guangzhou-5",
            "SlaveZones": [
                "ap-guangzhou-3"
            ],
            "InstanceSet": [
                {
                    "InstanceId": "cynosdbmysql-ins-abcd1235",
                    "InstanceName": "cynosdbmysql-用户自定义名称",
                    "InstanceType": "rw",
                    "InstanceStatus": "running",
                    "InstanceStatusDesc": "运行中",
                    "InstanceCpu": 1,
                    "InstanceMemory": 2,
                    "InstanceStorage": 0,
                    "InstanceRole": "master",
                    "MaintainStartTime": 0,
                    "MaintainDuration": 0,
                    "MaintainWeekDays": [
                        "Mon"
                    ],
                    "ServerlessStatus": "pause"
                }
            ],
            "PayMode": 0,
            "PeriodEndTime": "2030-01-01 10:01:01",
            "ProjectID": 0,
            "ResourceTags": [
                {
                    "TagKey": "tagKey-1",
                    "TagValue": "tagValue-1"
                }
            ],
            "ProxyStatus": "running",
            "LogBin": "ON",
            "IsSkipTrade": "no",
            "PitrType": "redo_pitr",
            "IsOpenPasswordComplexity": "yes",
            "NetworkStatus": "whole_rdma",
            "ResourcePackages": [
                {
                    "PackageId": "package-abcd1234",
                    "PackageType": "CCU",
                    "DeductionPriority": 1
                }
            ],
            "RenewFlag": 0,
            "NetworkType": "whole_rdma",
            "SlaveZoneAttr": [
                {
                    "Zone": "ap-guangzhou-3",
                    "BinlogSyncWay": "async"
                }
            ]
        },
        "RequestId": "requestId-123456789"
    }
}
```

