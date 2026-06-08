**Example 1: 创建实例请求**



Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --TypeId 18 \
    --MemSize 1024 \
    --GoodsNum 1 \
    --Period 1 \
    --BillingMode 0 \
    --ZoneId 100002 \
    --Password ******MyP*ssword \
    --VpcId vpc-pxyz**** \
    --SubnetId subnet-26qr**** \
    --RedisShardNum 3 \
    --RedisReplicasNum 1 \
    --NodeSet.0.NodeId 675 \
    --NodeSet.0.NodeType 0 \
    --NodeSet.0.ZoneId 100002 \
    --NodeSet.0.ZoneName ap-guangzhou-2 \
    --NodeSet.1.NodeId 676 \
    --NodeSet.1.NodeType 1 \
    --NodeSet.1.ZoneId 100003 \
    --NodeSet.1.ZoneName ap-guangzhou-3 \
    --ResourceTags.0.TagKey None \
    --ResourceTags.0.TagValue None \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "DealId": "20250825297021530591847",
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522",
        "InstanceIds": [
            "crs-bzss****"
        ]
    }
}
```

