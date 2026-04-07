**Example 1: 示例1**

创建7.0集群版实例

Input: 

```
tccli redis CreateInstances --cli-unfold-argument  \
    --TypeId 18 \
    --MemSize 2048 \
    --GoodsNum 1 \
    --Period 1 \
    --BillingMode 1 \
    --ZoneId 100002 \
    --Password Test123456 \
    --VpcId vpc-9uaohp0t \
    --SubnetId subnet-f7jqw3is \
    --SecurityGroupIdList sg-1kod56y5 \
    --RedisShardNum 1 \
    --RedisReplicasNum 1 \
    --InstanceName 123333
```

Output: 
```
{
    "Response": {
        "DealName": "20260407296022526727811",
        "InstanceIds": [
            "crs-lqz7y86j"
        ],
        "RequestId": "cb2278fb-abaf-4311-b23b-194363422ef3"
    }
}
```

