**Example 1: 购买主实例**

购买主实例

Input: 

```
tccli cdb CreateDBInstance --cli-unfold-argument  \
    --ResourceTags.0.TagKey march \
    --ResourceTags.0.TagValue march1 \
    --Zone ap-guangzhou-3 \
    --UniqVpcId vpc-0akbol5v \
    --ProjectId 0 \
    --InstanceRole master \
    --GoodsNum 1 \
    --Period 1 \
    --Volume 25 \
    --EngineVersion 5.6 \
    --UniqSubnetId subnet-fyrtjbqw \
    --Memory 1000 \
    --InstanceNodes 2
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "InstanceIds": [
            "cdb-pn6gd5jp"
        ],
        "DealIds": [
            "20171201110011"
        ]
    }
}
```

**Example 2: 购买只读实例**

购买只读实例

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

创建实例时设置表名大小写敏感

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

