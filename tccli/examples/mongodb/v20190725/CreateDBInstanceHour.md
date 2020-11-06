**Example 1: 创建云数据库实例（按量计费）**



Input: 

```
tccli mongodb CreateDBInstanceHour --cli-unfold-argument  \
    --Memory 4 \
    --Volume 250 \
    --ReplicateSetNum 1 \
    --NodeNum 2 \
    --MongoVersion MONGO_3_WT \
    --MachineCode TGIO \
    --GoodsNum 1 \
    --Zone ap-guangzhou-3 \
    --Clone 1 \
    --ClusterType REPLSET
```

Output: 
```
{
    "Response": {
        "RequestId": "eaf9b19d-5ad4-4ca2-9fc4-a319aeb9181f",
        "DealId": "20190709160000003502416120946732",
        "InstanceIds": [
            "cmgo-m26c6jsf"
        ]
    }
}
```

