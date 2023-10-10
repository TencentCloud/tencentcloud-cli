**Example 1: 修改策略可用状态接口**

根据策略id修改策略的可用状态

Input: 

```
tccli cwp ChangeStrategyEnableStatus --cli-unfold-argument  \
    --StrategyId 1 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

