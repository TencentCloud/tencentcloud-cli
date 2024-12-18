**Example 1: 创建包年包月的云数据库实例**

客户需要通过API创建包年包月云数据库实例

Input: 

```
tccli mongodb CreateDBInstance --cli-unfold-argument  \
    --Zone ap-guangzhou-2 \
    --UniqVpcId vpc-0akbol5v \
    --TimeSpan 1 \
    --ProjectId 0 \
    --MachineCode TGIO \
    --GoodsNum 1 \
    --Volume 250 \
    --SecondaryNum 2 \
    --UniqSubnetId subnet-fyrtjbqw \
    --Memory 4 \
    --MongoVersion MONGO_42_WT \
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

