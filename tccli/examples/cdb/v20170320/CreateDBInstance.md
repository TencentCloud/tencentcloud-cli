**Example 1: 购买主实例**



Input: 

```
tccli cdb CreateDBInstance --cli-unfold-argument  \
    --Memory 1000 \
    --Volume 25 \
    --Period 1 \
    --GoodsNum 1 \
    --Zone ap-guangzhou-3 \
    --UniqVpcId vpc-0akbol5v \
    --UniqSubnetId subnet-fyrtjbqw \
    --ProjectId 0 \
    --InstanceRole master \
    --EngineVersion 5.6 \
    --ResourceTags.0.TagKey marchtest \
    --ResourceTags.0.TagValue test1
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



Input: 

```
tccli cdb CreateDBInstance --cli-unfold-argument  \
    --MasterInstanceId cdb-fn3f9xpx \
    --Period 1 \
    --GoodsNum 1 \
    --Memory 4000 \
    --Volume 100 \
    --InstanceRole ro \
    --RoGroup.RoGroupMode allinone \
    --RoGroup.RoGroupName jersey_test \
    --RoGroup.RoOfflineDelay 1 \
    --RoGroup.RoMaxDelayTime 5 \
    --RoGroup.MinRoInGroup 1
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

