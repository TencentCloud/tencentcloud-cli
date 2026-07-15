**Example 1: 创建云数据库实例（按量计费）**

当前示例仅适合4.0版本，其余版本请严格参考传入参数中各版本说明项

Input: 

```
tccli mongodb CreateDBInstanceHour --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --GoodsNum 1 \
    --Clone 1 \
    --Memory 4 \
    --ClusterType REPLSET \
    --Volume 250 \
    --NodeNum 2 \
    --ReplicateSetNum 1 \
    --MachineCode HIO10G \
    --MongoVersion MONGO_40_WT
```

Output: 
```
{
    "Response": {
        "RequestId": "eaf9b19d-5ad4-4ca2-9fc4-a319aeb9181f",
        "DealId": "20190709160000003502416120946732",
        "InstanceIds": [
            "cmgo-m26c****"
        ]
    }
}
```

