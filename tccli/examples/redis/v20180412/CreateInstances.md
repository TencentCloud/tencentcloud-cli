**Example 1: 请求示例一**

购买包年包月的Redis5.0内存版（集群架构）实例

Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --TypeId 9 \
    --VpcId vpc-fmh***** \
    --GoodsNum 1 \
    --RedisShardNum 3 \
    --Period 3 \
    --BillingMode 1 \
    --NoAuth true \
    --MemSize 2048 \
    --SubnetId subnet-680c**** \
    --RedisReplicasNum 1 \
    --ZoneId 200002
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

**Example 2: 请求示例二**

购买按量计费的Redis4.0内存版（标准架构）实例

Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --TypeId 6 \
    --Password ********** \
    --GoodsNum 1 \
    --Period 1 \
    --BillingMode 0 \
    --MemSize 1024 \
    --ZoneId 100002
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

