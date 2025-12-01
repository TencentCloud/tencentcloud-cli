**Example 1: 创建云数据库实例（按量计费）**

创建云数据库实例（按量计费）

Input: 

```
tccli cdb CreateDBInstanceHour --cli-unfold-argument  \
    --GoodsNum 1 \
    --Memory 1000 \
    --Volume 200 \
    --UniqVpcId vpc-grpykq9v \
    --UniqSubnetId subnet-aq06sf6a \
    --Zone ap-guangzhou-ziyan3 \
    --InstanceRole master \
    --MasterRegion ap-guangzhou \
    --Port 3306 \
    --Password 190228bh \
    --ProtectMode 1 \
    --DeployMode 0 \
    --SlaveZone ap-guangzhou-ziyan3 \
    --SecurityGroup sg-9c3k3gtd \
    --RoGroup.RoGroupMode alone \
    --InstanceName test_creat_api \
    --InstanceNodes 2 \
    --Cpu 1 \
    --ParamTemplateType HIGH_STABILITY \
    --EngineType InnoDB
```

Output: 
```
{
    "Response": {
        "DealIds": [
            "20251117217021754869911"
        ],
        "InstanceIds": [
            "cdb-lw4ulca3"
        ],
        "RequestId": "0b330f82-f9a6-4f18-b048-cf7b42c8cec0"
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

