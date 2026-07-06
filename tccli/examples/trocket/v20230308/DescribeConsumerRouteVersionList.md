**Example 1: 查询消费组灰度路由配置版本列表成功**



Input: 

```
tccli trocket DescribeConsumerRouteVersionList --cli-unfold-argument  \
    --Topic test_topic \
    --InstanceId rmq-16je7x5e7o \
    --Group test_group
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Versions": [
            {
                "CutTimestamp": 1782730693958,
                "Rules": [
                    {
                        "MatchCondition": "test_tagC",
                        "TargetConsumerLabel": "test_env"
                    }
                ],
                "UpdatedAt": 1782730693958,
                "Version": 1
            }
        ],
        "RequestId": "68ff3f86-99a7-4df5-80b3-9eb7e9ec8edd"
    }
}
```

