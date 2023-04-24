**Example 1: 创建云数据库实例（按量计费）**

创建云数据库实例（按量计费）

Input: 

```
tccli cdb CreateDBInstanceHour --cli-unfold-argument  \
    --ResourceTags.0.TagKey marchtest \
    --ResourceTags.0.TagValue test1 \
    --Zone ap-guangzhou-3 \
    --UniqVpcId vpc-0akbol5v \
    --ProjectId 0 \
    --SlaveZone ap-guangzhou-3 \
    --InstanceRole master \
    --GoodsNum 1 \
    --DeployMode 0 \
    --Volume 25 \
    --EngineVersion 5.6 \
    --UniqSubnetId subnet-fyrtjbqw \
    --Memory 1000 \
    --ProtectMode 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "InstanceIds": [
            "cdb-03brtubb"
        ],
        "DealIds": [
            "20171201160000002670226599824833"
        ]
    }
}
```

