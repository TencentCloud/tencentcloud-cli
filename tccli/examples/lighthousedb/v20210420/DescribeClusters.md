**Example 1: 查询集群列表**

查询集群

Input: 

```
tccli lighthousedb DescribeClusters --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100 \
    --Filter.Name ClusterName \
    --Filter.Values  \
    --Filter.ExactMatch False
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Clusters": [
            {
                "ClusterId": "cynosdbmysql-abcdefgh",
                "ClusterName": "test_cluster",
                "DbType": "MYSQL",
                "DbVersion": "5.7",
                "Status": "running",
                "StatusDesc": "运行中",
                "PeriodEndTime": "2099-12-31 23:59:59",
                "CreateTime": "2000-01-01 00:00:00",
                "UpdateTime": "2020-12-01 12:00:00",
                "Cpu": 0,
                "Mem": 0,
                "StorageLimit": 0,
                "Vip": "123.234.12.123",
                "Vport": 12345,
                "WanStatus": "init",
                "WanDomain": "a.com",
                "WanIp": "12.23.34.5",
                "WanPort": 2234,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "RenewFlag": 0
            }
        ],
        "RequestId": "req-123456789"
    }
}
```

