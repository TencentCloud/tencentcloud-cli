**Example 1: Sample request**



Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --ZoneId 100002\
    --TypeId 2\
    --MemSize 1024\
    --GoodsNum 1\
    --Period 1\
    --Password ********\
    --BillingMode 1
```

Output: 
```
{
    "Response": {
        "DealId": "123456",
        "RequestId": "d4e2fd95-eac5-41ef-a7a9-7d30024d5507"
    }
}
```

**Example 2: 请求示例：购买包年包月的Redis5.0内存版（集群架构）实例**



Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --ZoneId 200002\
    --TypeId 9\
    --MemSize 2048\
    --GoodsNum 1\
    --Period 3\
    --BillingMode 1\
    --VpcId vpc-fmh*****\
    --SubnetId subnet-680c****\
    --RedisShardNum 3\
    --RedisReplicasNum 1\
    --NoAuth true
```

Output: 
```
{
    "Response": {
        "DealId": "154494263",
        "InstanceIds": [
            "crs-h9sn****"
        ],
        "RequestId": "d39baee1-e34f-4685-a810-5d27c510acb3"
    }
}
```

