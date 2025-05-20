**Example 1: 创建云数据库实例（按量计费）**

创建云数据库实例（按量计费）

Input: 

```
tccli cdb CreateDBInstanceHour --cli-unfold-argument  \
    --ResourceTags.0.TagKey march \
    --ResourceTags.0.TagValue march1 \
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

**Example 2: 创建实例时设置表名大小写敏感**

创建实例时设置表名大小写敏感

Input: 

```
tccli cdb CreateDBInstanceHour --cli-unfold-argument  \
    --GoodsNum 1 \
    --Memory 1000 \
    --Volume 25 \
    --EngineVersion 8.0 \
    --UniqVpcId vpc-4pagx2lk \
    --UniqSubnetId subnet-a2eaqb1t \
    --Zone ap-beijing-3 \
    --InstanceRole master \
    --ParamList.0.Name lower_case_table_names \
    --ParamList.0.Value 0 \
    --DeviceType UNIVERSAL \
    --Cpu 1 \
    --EngineType InnoDB
```

Output: 
```
{
    "Response": {
        "RequestId": "6166b535-64e8-4372-86fc-d6e26791f4fc",
        "InstanceIds": [
            "cdb-grq223rc"
        ],
        "DealIds": [
            "20250519054092411681522"
        ]
    }
}
```

