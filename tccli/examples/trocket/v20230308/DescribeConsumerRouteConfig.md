**Example 1: 查询消费组当前生效的灰度路由配置成功**



Input: 

```
tccli trocket DescribeConsumerRouteConfig --cli-unfold-argument  \
    --Topic test_topic \
    --InstanceId rmq-16je7x5e7o \
    --Group test_group
```

Output: 
```
{
    "Response": {
        "CutTimestamp": 1782730693958,
        "Rules": [
            {
                "MatchCondition": "test_tagC",
                "TargetConsumerLabel": "test_env"
            }
        ],
        "Version": 1,
        "RequestId": "149126a6-3eb1-4120-b81a-d86425fb9e3a"
    }
}
```

