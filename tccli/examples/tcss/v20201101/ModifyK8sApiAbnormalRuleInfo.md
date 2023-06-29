**Example 1: 修改k8sapi异常规则信息**



Input: 

```
tccli tcss ModifyK8sApiAbnormalRuleInfo --cli-unfold-argument  \
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
    --RuleInfo.RuleName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd"
    }
}
```

