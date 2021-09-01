**Example 1: 批量删除生命周期规则**

批量删除生命周期规则

Input: 

```
tccli chdfs DeleteLifeCycleRules --cli-unfold-argument  \
    --LifeCycleRuleIds 1 2
```

Output: 
```
{
    "Response": {
        "RequestId": "b629358c-ed40-4747-9060-3fcd34a8f32f"
    }
}
```

