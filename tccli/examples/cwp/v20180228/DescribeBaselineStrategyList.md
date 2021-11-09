**Example 1: 用户基线策略列表查询**

根据appid查询用户下全部的策略信息

Input: 

```
tccli cwp DescribeBaselineStrategyList --cli-unfold-argument  \
    --Enabled 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "f1dd9f5e-4ac0-48a7-9410-c86d24656d9a",
        "TotalCount": 2,
        "StrategyList": [
            {
                "StrategyName": "策略名",
                "StrategyId": "策略id",
                "HostCount": 50,
                "ScanCycle": 3,
                "ScanAt": "00,00,00",
                "Enabled": 1
            },
            {
                "StrategyName": "策略名2",
                "StrategyId": "策略id",
                "HostCount": 60,
                "ScanCycle": 3,
                "ScanAt": "12,00,00",
                "Enabled": 1
            }
        ]
    }
}
```

