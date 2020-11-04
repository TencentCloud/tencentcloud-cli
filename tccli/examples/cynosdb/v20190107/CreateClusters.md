**Example 1: 创建集群**



Input: 

```
tccli cynosdb CreateClusters --cli-unfold-argument  \
    --Zone ap-guangzhou-3\
    --ProjectId 0\
    --VpcId vpc-1ptuei0b\
    --SubnetId subnet-1tmw9t4o\
    --DbType POSTGRESQL\
    --DbVersion 10.0\
    --Cpu 2\
    --Memory 4\
    --Storage 100\
    --ClusterName newInstance\
    --AdminPassword passwd@admin\
    --HaCount 1\
    --Count 1\
    --PayMode 0\
    --RollbackStrategy noneRollback\
    --StorageLimit 100
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "cynosdbpg-ins-67rmucgk"
        ],
        "RequestId": "132075",
        "TranId": "20190522160000003106844584180998",
        "ClusterIds": [
            "cynosdbmysql-sls-9nts65r2"
        ],
        "BigDealIds": [
            "xxx"
        ],
        "DealNames": [
            "20190522112283"
        ]
    }
}
```

