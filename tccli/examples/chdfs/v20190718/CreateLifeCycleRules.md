**Example 1: 批量创建生命周期规则**

批量创建生命周期规则

Input: 

```
tccli chdfs CreateLifeCycleRules --cli-unfold-argument  \
    --FileSystemId f4mhaqkciq0 \
    --LifeCycleRules.0.LifeCycleRuleName test1 \
    --LifeCycleRules.0.Path /test1 \
    --LifeCycleRules.0.Transition.0.Days 7 \
    --LifeCycleRules.0.Transition.0.Type 1 \
    --LifeCycleRules.0.Status 1 \
    --LifeCycleRules.1.LifeCycleRuleName test2 \
    --LifeCycleRules.1.Path /test2 \
    --LifeCycleRules.1.Transition.0.Days 7 \
    --LifeCycleRules.1.Transition.0.Type 1 \
    --LifeCycleRules.1.Transition.1.Days 7 \
    --LifeCycleRules.1.Transition.1.Type 2 \
    --LifeCycleRules.1.Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5d6d3ef8-db1d-40de-afa1-d340302458bb"
    }
}
```

