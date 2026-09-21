**Example 1: 批量查询消费组灰度标签路由成功**



Input: 

```
tccli trocket DescribeConsumerLabelRoutes --cli-unfold-argument  \
    --InstanceId rmq-1****jjdr \
    --Labels.0.Group grp-5e551b \
    --Labels.0.Label rn5e551b
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Results": [
            {
                "Key": {
                    "Group": "grp-5e551b",
                    "Label": "rn5e551b"
                },
                "Routes": [
                    {
                        "Topic": "tp-5e551b",
                        "MatchCondition": "****",
                        "TargetConsumerLabel": "rn5e551b"
                    }
                ]
            }
        ],
        "RequestId": "f13f4abd-9204-43a4-9494-6ebbfaf14c41"
    }
}
```

