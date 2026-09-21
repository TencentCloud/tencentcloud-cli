**Example 1: 批量写入消费组灰度路由配置成功**



Input: 

```
tccli trocket PutConsumerRouteConfigs --cli-unfold-argument  \
    --InstanceId rmq-1****jjdr \
    --Configs.0.Topic tp-f4b91d \
    --Configs.0.Group grp-f4b91d \
    --Configs.0.Rules.0.MatchCondition **** \
    --Configs.0.Rules.0.TargetConsumerLabel waf4b91d
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "FailedCount": 0,
        "Failures": [],
        "RequestId": "be77bad0-5b6b-44f4-9419-5a53b7a91085"
    }
}
```

