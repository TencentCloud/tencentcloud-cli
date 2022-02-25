**Example 1: 创建包年包月的云数据库实例**

当前示例仅适合4.0版本，其余版本请严格参考传入参数中各版本说明项

Input: 

```
tccli mongodb CreateDBInstance --cli-unfold-argument  \
    --Memory 4 \
    --Volume 250 \
    --GoodsNum 1 \
    --Zone ap-guangzhou-2 \
    --VpcId vpc-0akbol5v \
    --SubnetId subnet-fyrtjbqw \
    --ProjectId 0 \
    --MongoVersion MONGO_40_WT \
    --MachineCode HIO10G \
    --NodeNum 3 \
    --Period 1 \
    --Password pwd123456 \
    --ClusterType REPLSET \
    --ReplicateSetNum 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d88095e5-50e8-4245-a0cf-993a536f9b20",
        "DealId": "7142863",
        "InstanceIds": [
            "cmgo-po5f899l"
        ]
    }
}
```

