**Example 1: 新增或修改企微机器人规则**

新增或修改企微机器人规则

Input: 

```
tccli cwp ModifyWebHookRule --cli-unfold-argument  \
    --Data.RuleName 测试机器人 \
    --Data.HookAddr https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=747c393e-f771-47ca-af0a-cc36b88f107a \
    --Data.RuleRemark  \
    --Data.RuleItems.0.Type 2 \
    --Data.RuleItems.0.ControlBit 01111 \
    --Data.IsDisabled 1 \
    --Data.RuleId 55
```

Output: 
```
{
    "Response": {
        "RequestId": "747c393e-f771-47ca-af0a-cc36b88f107a"
    }
}
```

