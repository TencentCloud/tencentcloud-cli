**Example 1: 查询镜像拦截规则统计**



Input: 

```
tccli tcss DescribeImageDenyRuleSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EnabledRuleCount": 1,
        "RuleTotalCount": 1,
        "EffectiveRuleCount": 1,
        "RequestId": "xx",
        "ObservedRuleCount": 1
    }
}
```

