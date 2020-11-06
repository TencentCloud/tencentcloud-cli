**Example 1: 批量修改生命周期规则属性**

批量修改生命周期规则属性

Input: 

```
tccli chdfs ModifyLifeCycleRules --cli-unfold-argument  \
    --LifeCycleRules.0.LifeCycleRuleId 1 \
    --LifeCycleRules.0.LifeCycleRuleName test1 \
    --LifeCycleRules.0.Status 1 \
    --LifeCycleRules.1.LifeCycleRuleId 2 \
    --LifeCycleRules.1.Path /test2 \
    --LifeCycleRules.1.Transition.0.Days 7 \
    --LifeCycleRules.1.Transition.0.Type 1 \
    --LifeCycleRules.1.Transition.1.Days 7 \
    --LifeCycleRules.1.Transition.1.Type 2
```

Output: 
```
{
    "Response": {
        "RequestId": "baaf73f9-0c42-441b-afdb-b9da71a50f47"
    }
}
```

