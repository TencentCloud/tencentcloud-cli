**Example 1: 创建包年包月的云数据库实例**

当前示例仅适合4.0版本，其余版本请严格参考传入参数中各版本说明项

Input: 

```
tccli mongodb CreateDBInstance --cli-unfold-argument  \
    --VpcId vpc-0akbol5v \
    --GoodsNum 1 \
    --Zone ap-guangzhou-2 \
    --ProjectId 0 \
    --MachineCode HIO10G \
    --Period 1 \
    --ClusterType REPLSET \
    --Volume 250 \
    --MongoVersion MONGO_40_WT \
    --NodeNum 3 \
    --ReplicateSetNum 1 \
    --Memory 4 \
    --SubnetId subnet-fyrtjbqw \
    --Password pwd123456
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

