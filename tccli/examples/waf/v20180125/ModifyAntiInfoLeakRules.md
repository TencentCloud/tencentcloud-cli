**Example 1: 编辑信息防泄漏规则**

编辑信息防泄漏规则

Input: 

```
tccli waf ModifyAntiInfoLeakRules --cli-unfold-argument  \
    --RuleId 167 \
    --Name test1 \
    --Domain www.test1.com \
    --ActionType 0 \
    --Strategies.0.Field information \
    --Strategies.0.CompareFunc contains \
    --Strategies.0.Content phone
```

Output: 
```
{
    "Response": {
        "RequestId": "640e40da-d57a-4402-8e3d-39c5bed8addd"
    }
}
```

