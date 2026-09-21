**Example 1: 批量查询消费组灰度路由配置成功示例**



Input: 

```
tccli trocket DescribeConsumerRouteConfigs --cli-unfold-argument  \
    --InstanceId rmq-1****jjdr \
    --Configs.0.Topic tp-fd746f \
    --Configs.0.Group grp-fd746f
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Results": [
            {
                "Key": {
                    "Topic": "tp-fd746f",
                    "Group": "grp-fd746f"
                },
                "Version": 1,
                "Rules": [
                    {
                        "MatchCondition": "grayFlag = '1'",
                        "TargetConsumerLabel": "l1fd746f"
                    }
                ],
                "CutTimestamp": 1789620229459
            }
        ],
        "RequestId": "306632c6-ddbc-409b-9c8e-e246f4f14209"
    }
}
```

