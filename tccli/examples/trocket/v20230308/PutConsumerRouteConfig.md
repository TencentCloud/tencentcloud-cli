**Example 1: 写入消费组灰度路由配置成功**



Input: 

```
tccli trocket PutConsumerRouteConfig --cli-unfold-argument  \
    --Topic test_topic \
    --InstanceId rmq-16je7x5e7o \
    --Group test_group \
    --Rules.0.MatchCondition test_tagA \
    --Rules.0.TargetConsumerLabel test_env
```

Output: 
```
{
    "Response": {
        "Group": "test_group",
        "InstanceId": "rmq-16je7x5e7o",
        "Topic": "test_topic",
        "Version": 1,
        "RequestId": "9bd61d2b-ffcc-4e2d-91f3-9c95ec852d9d"
    }
}
```

