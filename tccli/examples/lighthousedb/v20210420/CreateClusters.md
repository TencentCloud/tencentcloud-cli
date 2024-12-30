**Example 1: 创建集群**



Input: 

```
tccli lighthousedb CreateClusters --cli-unfold-argument  \
    --AdminPassword isd@cloud123 \
    --AutoRenewFlag 0 \
    --ClusterName lhdb_lhdb_20241230060506 \
    --Cpu 1 \
    --DbType MYSQL \
    --DbVersion 5.7 \
    --Memory 1 \
    --Port 3306 \
    --StorageLimit 40 \
    --TimeSpan 1 \
    --TimeUnit m
```

Output: 
```
{
    "Response": {
        "DealNames": [
            "20241230458077490098301"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

