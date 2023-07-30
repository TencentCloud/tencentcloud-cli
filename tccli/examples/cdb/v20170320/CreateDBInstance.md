**Example 1: 购买主实例**

购买主实例

Input: 

```
tccli cdb CreateDBInstance --cli-unfold-argument  \
    --ResourceTags.0.TagKey marchtest \
    --ResourceTags.0.TagValue test1 \
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
    --RoGroup.RoGroupName jersey_test \
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

