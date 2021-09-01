**Example 1: 创建云数据库实例（按量计费）**

客户需要通过API创建按量计费的云数据库实例

Input: 

```
tccli mongodb CreateDBInstanceHour --cli-unfold-argument  \
    --Memory 4 \
    --Volume 250 \
    --ReplicateSetNum 1 \
    --SecondaryNum 2 \
    --EngineVersion MONGO_3_WT \
    --Machine TGIO \
    --GoodsNum 1 \
    --Zone ap-guangzhou-3 \
    --InstanceRole MASTER \
    --InstanceType REPLSET
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

