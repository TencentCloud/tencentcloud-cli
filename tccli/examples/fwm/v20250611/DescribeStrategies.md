**Example 1: 查询策略列表**



Input: 

```
tccli fwm DescribeStrategies --cli-unfold-argument  \
    --Product enterprise_sg \
    --ExecArea pre \
    --Filters.0.Name GroupName \
    --Filters.0.OperatorType 9 \
    --Filters.0.Values 类型安全组 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6139ea4e-d67e-4bc6-a122-d71a6a339dac",
        "Strategies": [
            {
                "CreateBy": "100011616646",
                "CreateName": "天空之蓝",
                "CreateTime": "2026-02-27 19:06:59",
                "ErrMsg": "",
                "ErrorType": "",
                "ExecArea": "pre",
                "GroupId": "fwmrg-6wq0b6j0",
                "GroupName": "不同类型安全组下发",
                "ReceiveAccount": [
                    {
                        "Nickname": "天空之蓝",
                        "Uin": "100011616646"
                    }
                ],
                "RuleCount": 7,
                "RuleStatus": 1,
                "Sequence": 2,
                "StrategyId": "fwms-ms91jjvy",
                "UpdateBy": "100011616646",
                "UpdateName": "天空之蓝",
                "UpdateTime": "2026-02-27 19:52:50"
            },
            {
                "CreateBy": "100011616646",
                "CreateName": "天空之蓝",
                "CreateTime": "2026-02-27 19:22:44",
                "ErrMsg": "",
                "ErrorType": "",
                "ExecArea": "pre",
                "GroupId": "fwmrg-6wq0b6j0",
                "GroupName": "不同类型安全组下发",
                "ReceiveAccount": [
                    {
                        "Nickname": "天空之蓝",
                        "Uin": "100011616646"
                    }
                ],
                "RuleCount": 7,
                "RuleStatus": 1,
                "Sequence": 3,
                "StrategyId": "fwms-vg9ji1r5",
                "UpdateBy": "100011616646",
                "UpdateName": "天空之蓝",
                "UpdateTime": "2026-02-27 19:52:50"
            }
        ],
        "TotalCount": 2
    }
}
```

