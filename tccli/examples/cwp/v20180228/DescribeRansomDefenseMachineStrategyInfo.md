**Example 1: 获取主机绑定策略列表**



Input: 

```
tccli cwp DescribeRansomDefenseMachineStrategyInfo --cli-unfold-argument  \
    --Quuids 935e27b1-d675-4509-80bf-96fbf0764237
```

Output: 
```
{
    "Response": {
        "RequestId": "935e27b1-d675-4509-80bf-96fbf0764237",
        "StrategyIds": [
            1
        ]
    }
}
```

