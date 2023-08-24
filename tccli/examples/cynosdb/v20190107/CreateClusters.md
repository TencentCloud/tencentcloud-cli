**Example 1: 购买新集群**

购买新集群

Input: 

```
tccli cynosdb CreateClusters --cli-unfold-argument  \
    --Count 1 \
    --StoragePayMode 0 \
    --VpcId vpc-1ptuei0b \
    --Zone ap-guangzhou-3 \
    --AdminPassword passwd@admin \
    --DbType MYSQL \
    --ProjectId 0 \
    --DbVersion 10.0 \
    --Storage 100 \
    --PayMode 0 \
    --ClusterName newInstance \
    --StorageLimit 100 \
    --RollbackStrategy noneRollback \
    --Memory 4 \
    --SubnetId subnet-1tmw9t4o \
    --Cpu 2 \
    --HaCount 1
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "cynosdbmysql-ins-67rmucgk"
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

