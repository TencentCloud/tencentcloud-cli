**Example 1: 购买主实例**



Input: 

```
tccli cdb CreateDBInstance --cli-unfold-argument  \
    --Memory 1000 \
    --Volume 200 \
    --Period 12 \
    --GoodsNum 1 \
    --Zone ap-guangzhou-ziyan3 \
    --UniqVpcId vpc-grpykq9v \
    --UniqSubnetId subnet-aq06sf6a \
    --Port 3306 \
    --InstanceRole master \
    --Password 190228bh \
    --ProtectMode 1 \
    --DeployMode 0 \
    --SlaveZone ap-guangzhou-ziyan3 \
    --SecurityGroup sg-9c3k3gtd \
    --InstanceName test_create-api2 \
    --InstanceNodes 2 \
    --Cpu 1 \
    --EngineType InnoDB
```

Output: 
```
{
    "Response": {
        "DealIds": [
            "20251117217021754844851"
        ],
        "InstanceIds": [
            "cdb-4wixd9pn"
        ],
        "RequestId": "bae642bd-305a-40fe-b64c-356dc809977b"
    }
}
```

**Example 2: 购买只读实例**



Input: 

```
tccli cdb CreateDBInstance --cli-unfold-argument  \
    --RoGroup.RoGroupMode allinone \
    --RoGroup.RoGroupName jersey \
    --RoGroup.RoMaxDelayTime 5 \
    --RoGroup.MinRoInGroup 1 \
    --RoGroup.RoOfflineDelay 1 \
    --GoodsNum 1 \
    --InstanceRole ro \
    --MasterInstanceId cdb-fn3f9xpx \
    --Period 1 \
    --Volume 100 \
    --Memory 4000
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "DealIds": [
            "20171205110051"
        ],
        "InstanceIds": [
            "cdbro-hlpl4ik9"
        ]
    }
}
```

**Example 3: 创建实例时设置表名大小写敏感**



Input: 

```
tccli cdb CreateDBInstance --cli-unfold-argument  \
    --Memory 1000 \
    --Volume 25 \
    --Period 1 \
    --GoodsNum 1 \
    --Zone ap-beijing-3 \
    --UniqVpcId vpc-4pagx2lk \
    --UniqSubnetId subnet-a2eaqb1t \
    --InstanceRole master \
    --EngineVersion 8.0 \
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
        "RequestId": "6166b535-64e8-4372-86fc-d6e25791f4fc",
        "InstanceIds": [
            "cdb-grq113rc"
        ],
        "DealIds": [
            "20250519054092411681521"
        ]
    }
}
```

