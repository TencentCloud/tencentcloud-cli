**Example 1: 策略名查询策略**

根据策略名查询策略是否已存在

Input: 

```
tccli cwp DescribeStrategyExist --cli-unfold-argument  \
    --StrategyName "策略1"
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "IfExist": 1
    }
}
```

