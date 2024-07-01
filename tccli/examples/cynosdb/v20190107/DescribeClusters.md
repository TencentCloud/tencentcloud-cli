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
                    "IsSupportManualSnapshot": "",
                    "IsSupportRo": "yes",
                    "IsSupportSlaveZone": "yes",
                    "IsSupportTransparentDataEncryption": "",
                    "NoSupportTransparentDataEncryptionReason": "",
                    "NonsupportRoReason": "",
                    "NonsupportSlaveZoneReason": ""
                },
                "AppId": 123,
                "BusinessType": "",
                "ClusterId": "cynosdbmysql-aaa",
                "ClusterName": "resource-xxl-job-intl",
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
                        "Description": "",
                        "InstanceGroupId": "",
                        "NetType": "singleRo",
                        "UniqSubnetId": "subnet-xx",
                        "UniqVpcId": "vpc-xx",
                        "Vip": "1.1.1.1",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": "init"
                    },
                    {
                        "Description": "",
                        "InstanceGroupId": "",
                        "NetType": "ha",
                        "UniqSubnetId": "subnet-xx",
                        "UniqVpcId": "vpc-xx",
                        "Vip": "1.1.1.1",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": "init"
                    },
                    {
                        "Description": "",
                        "InstanceGroupId": "",
                        "NetType": "proxy",
                        "UniqSubnetId": "subnet-xx",
                        "UniqVpcId": "vpc-xx",
                        "Vip": "1.1.1.1",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": ""
                    }
                ],
                "OrderSource": "",
                "PayMode": 1,
                "PeriodEndTime": "2024-06-30 19:32:51",
                "PhysicalZone": "ap-singapore-3",
                "ProcessingTask": "",
                "ProjectID": 0,
                "Region": "ap-singapore",
                "RenewFlag": 1,
                "ResourcePackages": [],
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
                "ServerlessStatus": "",
                "SlaveZones": [
                    "ap-singapore-4"
                ],
                "Status": "running",
                "StatusDesc": "运行中",
                "Storage": 0,
                "StorageId": "",
                "StorageLimit": 30000,
                "StoragePayMode": 0,
                "SubnetId": "subnet-xx",
                "Tasks": [],
                "Uin": "1234",
                "UpdateTime": "2024-05-30 19:43:06",
                "Vip": "1.1.1.1",
                "VpcId": "vpc-xx",
                "Vport": 3306,
                "Zone": "ap-singapore-3"
            }
        ],
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923",
        "TotalCount": 31
    }
}
```

