**Example 1: 查询基线默认策略列表信息**

查询用户下的默认策略信息列表

Input: 

```
tccli cwp DescribeBaselineDefaultStrategyList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "StrategyList": [
            {
                "StrategyName": "策略名",
                "StrategyId": 1
            },
            {
                "StrategyName": "策略名2",
                "StrategyId": 2
            }
        ]
    }
}
```

