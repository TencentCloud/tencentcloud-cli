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
            "ClusterId": "cynosdbmysql-sgvwu2is",
            "ClusterName": "cynodbmysql-自定义用户名",
            "Region": "ap-guangzhou",
            "Zone": "ap-guangzhou-5",
            "PhysicalZone": "ap-guangzhou-5",
            "Status": "running",
            "StatusDesc": "运行中",
            "ServerlessStatus": "运行中",
            "StorageId": "cynosdbmysql-sgvwu2is",
            "Storage": 20,
            "MaxStorageSize": 1000,
            "MinStorageSize": 10,
            "StoragePayMode": 0,
            "VpcName": "vpc-osjw7wbx",
            "VpcId": "vpc-osjw7wbx",
            "SubnetName": "subnet-stbcji8s",
            "SubnetId": "subnet-stbcji8s",
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
            "HasSlaveZone": "yes",
            "IsFreeze": "no",
            "Tasks": [
                {
                    "TaskId": 10,
                    "TaskType": "taskAutoBackup",
                    "TaskStatus": "processing",
                    "ObjectId": "cynosdbmysql-sgvwu2is",
                    "ObjectType": "taskObjTypeCluster"
                }
            ],
            "MasterZone": "ap-guangzhou-5",
            "SlaveZones": [
                "ap-guangzhou-3"
            ],
            "InstanceSet": [
                {
                    "InstanceId": "cynosdbmysql-ins-xvs9osn2",
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
                    "PackageId": "package-xbhsw7wk",
                    "PackageType": "CCU",
                    "DeductionPriority": 1
                }
            ],
            "RenewFlag": 0,
            "NetworkType": "whole_rdma",
            "SlaveZoneAttr": [
                {
                    "Zone": "ap-guangzhou-3",
                    "BinlogSyncWay": "async",
                    "SemiSyncTimeout": 10000
                }
            ]
        },
        "RequestId": "6febb6f0-b0fc-11ee-93cb-73a07daf38c5"
    }
}
```

