**Example 1: 查看弹性伸缩策略列表**

查看弹性伸缩策略列表

Input: 

```
tccli tse DescribeAutoScalerResourceStrategies --cli-unfold-argument  \
    --GatewayId gateway-4a34cf5f
```

Output: 
```
{
    "Response": {
        "RequestId": "adc44984-762c-42e0-b39a-80777e5c3bcc",
        "Result": {
            "TotalCount": 1,
            "StrategyList": [
                {
                    "StrategyId": "strategy-7bb4fcb0",
                    "StrategyName": "test",
                    "CreateTime": "2021-09-09 11:52:30",
                    "ModifyTime": "2021-09-09 11:52:30",
                    "Description": "测试",
                    "GatewayId": "gateway-4a34cf5f",
                    "Config": {
                        "AutoScalerId": "autoscaler-92aaca7b",
                        "StrategyId": "strategy-448e24f7",
                        "Enabled": true,
                        "MaxReplicas": 15,
                        "Metrics": [
                            {
                                "Type": "Resource",
                                "ResourceName": "cpu",
                                "TargetType": "Utilization",
                                "TargetValue": 50
                            },
                            {
                                "Type": "Pods",
                                "ResourceName": "tcp-connection-num",
                                "TargetType": "AverageValue",
                                "TargetValue": 5
                            }
                        ],
                        "CreateTime": "2023-03-08 16:57:18",
                        "ModifyTime": "2023-03-08 16:57:18"
                    },
                    "CronConfig": {
                        "StrategyId": "strategy-448e24f7",
                        "Enabled": true,
                        "Params": [
                            {
                                "Period": "",
                                "StartAt": "17:00",
                                "TargetReplicas": 0
                            }
                        ],
                        "CreateTime": "2023-03-08 16:57:18",
                        "ModifyTime": "2023-03-08 16:57:18"
                    }
                }
            ]
        }
    }
}
```

