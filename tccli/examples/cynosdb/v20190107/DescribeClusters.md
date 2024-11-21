**Example 1: 查询集群列表**

查询集群列表

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
        "ClusterSet": [
            {
                "Ability": {
                    "IsSupportManualSnapshot": "no",
                    "IsSupportRo": "yes",
                    "IsSupportSlaveZone": "yes",
                    "IsSupportTransparentDataEncryption": "no",
                    "NoSupportTransparentDataEncryptionReason": "current cluster not support transparent data encryption",
                    "NonsupportRoReason": "yes",
                    "NonsupportSlaveZoneReason": "current cluster not support ro"
                },
                "AppId": 2372636427,
                "BusinessType": "bus_a",
                "ClusterId": "cynosdbmysql-cbsg6tsg",
                "ClusterName": "MyClusterName",
                "CreateTime": "2024-05-30 19:26:42",
                "CynosVersion": "2.1.12",
                "DbMode": "NORMAL",
                "DbType": "MYSQL",
                "DbVersion": "5.7",
                "HasSlaveZone": "yes",
                "InstanceNum": 2,
                "IsFreeze": "no",
                "MasterZone": "ap-singapore-3",
                "MaxStorageSize": 30000,
                "MinStorageSize": 10,
                "NetAddrs": [
                    {
                        "Description": "descirption",
                        "InstanceGroupId": "cynosdbpg-grp-sbh6ywhs",
                        "NetType": "singleRo",
                        "UniqSubnetId": "subnet-cnhsb8iu",
                        "UniqVpcId": "vpc-iskx6ygc",
                        "Vip": "1.1.1.1",
                        "Vport": 3306,
                        "WanDomain": "cynosdbpg-bzbsxrmt.wan.domain.com",
                        "WanIP": "3.45.1.9",
                        "WanPort": 3306,
                        "WanStatus": "init"
                    },
                    {
                        "Description": "descirption",
                        "InstanceGroupId": "cynosdbpg-grp-bc2b3us4",
                        "NetType": "ha",
                        "UniqSubnetId": "subnet-7shw8ijc",
                        "UniqVpcId": "vpc-y7us28sn",
                        "Vip": "1.1.1.1",
                        "Vport": 3306,
                        "WanDomain": "cynosdbpg-bzkxxrmt.wan.domain.com",
                        "WanIP": "3.23.1.5",
                        "WanPort": 3306,
                        "WanStatus": "init"
                    }
                ],
                "OrderSource": "lhdb",
                "PayMode": 1,
                "PeriodEndTime": "2024-06-30 19:32:51",
                "PhysicalZone": "ap-singapore-3",
                "ProcessingTask": "taskUpgradeStorage",
                "ProjectID": 23,
                "Region": "ap-singapore",
                "RenewFlag": 1,
                "ResourcePackages": [
                    {
                        "DeductionPriority": 0,
                        "PackageId": "package-nxuyx1op",
                        "PackageType": "CCU"
                    }
                ],
                "ResourceTags": [
                    {
                        "TagKey": "运营产品",
                        "TagValue": "腾讯云计费产品其它_1649"
                    },
                    {
                        "TagKey": "运营部门",
                        "TagValue": "计费产品中心_1013"
                    },
                    {
                        "TagKey": "一级业务",
                        "TagValue": "[N][腾讯云计费产品其它]_979685"
                    },
                    {
                        "TagKey": "二级业务",
                        "TagValue": "[license管理][license数据引擎]123"
                    }
                ],
                "ServerlessStatus": "paused",
                "SlaveZones": [
                    "ap-singapore-4"
                ],
                "Status": "running",
                "StatusDesc": "运行中",
                "Storage": 0,
                "StorageId": "cynosdbpg-bcsu6tsg",
                "StorageLimit": 30000,
                "StoragePayMode": 0,
                "SubnetId": "subnet-ybs8jcnw",
                "Tasks": [
                    {
                        "ObjectId": "cynosdbmysql-k5sm8sh3",
                        "ObjectType": "taskObjTypeCluster",
                        "TaskId": 1207003,
                        "TaskStatus": "processing",
                        "TaskType": "taskDtsLockResource"
                    }
                ],
                "Uin": "237462834",
                "UpdateTime": "2024-05-30 19:43:06",
                "Vip": "1.1.1.1",
                "VpcId": "vpc-ybs8ue2y",
                "Vport": 3306,
                "Zone": "ap-singapore-3"
            }
        ],
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923",
        "TotalCount": 31
    }
}
```

