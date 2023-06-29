**Example 1: 创建k8sapi异常事件规则**



Input: 

```
tccli tcss CreateK8sApiAbnormalRuleInfo --cli-unfold-argument  \
    --RuleInfo.Status True \
    --RuleInfo.RuleInfoList.0.Action xx \
    --RuleInfo.RuleInfoList.0.Scope xx \
    --RuleInfo.RuleInfoList.0.RiskLevel xx \
    --RuleInfo.RuleInfoList.0.IsDelete True \
    --RuleInfo.RuleInfoList.0.Status True \
    --RuleInfo.EffectClusterIDSet xx \
    --RuleInfo.RuleID xx \
    --RuleInfo.RuleType xx \
    --RuleInfo.EffectAllCluster True \
    --RuleInfo.RuleName xx \
    --CopySrcRuleID xx
```

Output: 
```
{
    "Response": {
        "RuleID": "xxx",
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd"
    }
}
```

