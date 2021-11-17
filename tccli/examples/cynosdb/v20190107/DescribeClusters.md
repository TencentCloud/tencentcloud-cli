**Example 1: 查询集群列表**



Input: 

```
tccli cynosdb DescribeClusters --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --Filters.0.Names InstanceId \
    --Filters.0.Values cynosdbpg-ins-bzkxxrmt \
    --Filters.0.ExactMatch true \
    --DbType MYSQL
```

Output: 
```
{
    "Response": {
        "RequestId": "b81444b5-e558-4246-85be-d037937f93e0",
        "ClusterSet": [
            {
                "MaxStorageSize": 30000,
                "Status": "running",
                "VpcId": "vpc-mnkc86gd",
                "UpdateTime": "2021-11-15 21:48:37",
                "Region": "ap-guangzhou",
                "AppId": 251007582,
                "Tasks": [],
                "RenewFlag": 0,
                "PeriodEndTime": "2021-12-15 21:48:37",
                "ClusterId": "cynosdbmysql-49sxfmct",
                "CreateTime": "2021-11-15 21:47:50",
                "MinStorageSize": 10,
                "SubnetId": "subnet-kdqq63yu",
                "ClusterName": "预付费集群",
                "DbMode": "NORMAL",
                "StatusDesc": "运行中",
                "CynosVersion": "2.0.15",
                "ProcessingTask": "",
                "DbType": "MYSQL",
                "ProjectID": 0,
                "Uin": "100000007539",
                "ResourceTags": [],
                "DbVersion": "5.7",
                "StorageId": "",
                "StorageLimit": 30000,
                "NetAddrs": [
                    {
                        "WanDomain": "",
                        "NetType": "ha",
                        "Vport": 3306,
                        "WanPort": 0,
                        "Vip": "172.16.62.137"
                    },
                    {
                        "WanDomain": "",
                        "NetType": "ro",
                        "Vport": 3306,
                        "WanPort": 0,
                        "Vip": "172.16.62.176"
                    }
                ],
                "ServerlessStatus": "",
                "Zone": "ap-guangzhou-3",
                "StoragePayMode": 0,
                "InstanceNum": 1,
                "PayMode": 1,
                "Storage": 0,
                "Vport": 3306,
                "Vip": "172.16.62.137"
            }
        ],
        "TotalCount": 597
    }
}
```

