**Example 1: 创建集群**



Input: 

```
tccli cynosdb CreateClusters --cli-unfold-argument  \
    --Zone ap-guangzhou-5 \
    --VpcId 0 \
    --SubnetId 0 \
    --DbType MYSQL \
    --DbVersion 8.0 \
    --Cpu 1 \
    --Memory 1 \
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "BigDealIds": [],
        "ClusterIds": [
            "cynosdbmysql-********"
        ],
        "DealNames": [
            "2026*****************11"
        ],
        "RequestId": "7e55656e-37c6-44fe-9f81-34eafa652820",
        "ResourceIds": [
            "cynosdbmysql-ins-********"
        ],
        "TranId": "2026061198**5**9*8*****"
    }
}
```

