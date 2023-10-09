**Example 1: 获取主机绑定策略列表**



Input: 

```
tccli cwp DescribeRansomDefenseMachineStrategyInfo --cli-unfold-argument  \
    --Quuids xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "StrategyIds": [
            1
        ]
    }
}
```

