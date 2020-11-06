**Example 1: 请求示例：购买按量计费的Redis4.0内存版（标准架构）实例**



Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --ZoneId 100002 \
    --TypeId 6 \
    --MemSize 1024 \
    --GoodsNum 1 \
    --Period 1 \
    --BillingMode 0 \
    --Password **********
```

Output: 
```
{
    "Response": {
        "RequestId": "2a836c00-175f-11eb-aeb3-db134c8d8fec",
        "InstanceIds": [
            "crs-kic39axx"
        ],
        "DealId": "22716"
    }
}
```

**Example 2: 请求示例：购买包年包月的Redis5.0内存版（集群架构）实例**



Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --ZoneId 200002 \
    --TypeId 9 \
    --MemSize 2048 \
    --GoodsNum 1 \
    --Period 3 \
    --BillingMode 1 \
    --VpcId vpc-fmh***** \
    --SubnetId subnet-680c**** \
    --RedisShardNum 3 \
    --RedisReplicasNum 1 \
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

