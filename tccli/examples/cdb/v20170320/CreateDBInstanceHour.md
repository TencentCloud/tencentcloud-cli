**Example 1: 创建云数据库实例（按量计费）**



Input: 

```
tccli cdb CreateDBInstanceHour --cli-unfold-argument  \
    --Memory 1000\
    --Volume 25\
    --GoodsNum 1\
    --Zone ap-guangzhou-3\
    --UniqVpcId vpc-0akbol5v\
    --UniqSubnetId subnet-fyrtjbqw\
    --ProjectId 0\
    --InstanceRole master\
    --EngineVersion 5.6\
    --ProtectMode 0\
    --DeployMode 0\
    --SlaveZone ap-guangzhou-3\
    --ResourceTags.0.TagKey marchtest\
    --ResourceTags.0.TagValue test1
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

