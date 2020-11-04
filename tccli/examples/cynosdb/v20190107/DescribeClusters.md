**Example 1: 查询集群列表**



Input: 

```
tccli cynosdb DescribeClusters --cli-unfold-argument  \
    --Limit 20\
    --Offset 0\
    --Filters.0.Name InstanceId\
    --Filters.0.Values cynosdbpg-ins-bzkxxrmt\
    --DbType MYSQL
```

Output: 
```
{
    "Response": {
        "ClusterSet": [
            {
                "AppId": 1251006373,
                "ClusterId": "cynosdbpg-2x6bqwa0",
                "ClusterName": "cynosdbpg-2x6bqwa0",
                "CreateTime": "2019-02-14 14:23:57",
                "DbType": "POSTGRESQL",
                "DbVersion": "10.0",
                "InstanceNum": 1,
                "PayMode": 0,
                "PeriodEndTime": "2019-03-14 14:26:42",
                "Region": "ap-guangzhou",
                "Status": "running",
                "StatusDesc": "运行中",
                "Uin": "20548499",
                "UpdateTime": "2019-02-15 20:15:59",
                "Vip": "172.16.0.36",
                "Vport": 5432,
                "Zone": "ap-guangzhou-3"
            },
            {
                "AppId": 1251006373,
                "ClusterId": "cynosdbpg-6zd9ynyk",
                "ClusterName": "cynosdbpg-6zd9ynyk",
                "CreateTime": "2019-02-02 16:43:00",
                "DbType": "POSTGRESQL",
                "DbVersion": "10.0",
                "InstanceNum": 1,
                "PayMode": 0,
                "PeriodEndTime": "2019-03-02 16:43:00",
                "Region": "ap-guangzhou",
                "Status": "creating",
                "StatusDesc": "创建中",
                "Uin": "20548499",
                "UpdateTime": "2019-02-02 16:43:00",
                "Vip": "",
                "Vport": 5432,
                "Zone": "ap-guangzhou-3"
            },
            {
                "AppId": 1251006373,
                "ClusterId": "cynosdbpg-g6u0kj8m",
                "ClusterName": "cynosdbpg-g6u0kj8m",
                "CreateTime": "2019-02-02 16:33:51",
                "DbType": "POSTGRESQL",
                "DbVersion": "10.0",
                "InstanceNum": 1,
                "PayMode": 0,
                "PeriodEndTime": "2019-03-02 16:33:51",
                "Region": "ap-guangzhou",
                "Status": "creating",
                "StatusDesc": "创建中",
                "Uin": "20548499",
                "UpdateTime": "2019-02-02 16:33:51",
                "Vip": "",
                "Vport": 5432,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "a70bd8ff-b758-444c-8369-c6cd84c5239f",
        "TotalCount": 3
    }
}
```

