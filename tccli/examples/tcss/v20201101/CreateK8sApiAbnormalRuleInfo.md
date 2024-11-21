**Example 1: 创建k8sapi异常事件规则**



Input: 

```
tccli tcss CreateK8sApiAbnormalRuleInfo --cli-unfold-argument  \
    --RuleInfo.RuleName rulename1 \
    --RuleInfo.Status True \
    --RuleInfo.RuleInfoList.0.Scope {"RequestURI":"/apis/cowsajhhoa.k8s.io/v","RequestUser":"“name”:”sanpasahsad-contaosaer-leader”）\"","ResponseStatusCode":"200","SourceIPS":"10.255.0.43","UserAgent":"snapshot-controller","Verb":"update"} \
    --RuleInfo.RuleInfoList.0.Action RULE_MODE_ALERT \
    --RuleInfo.RuleInfoList.0.RiskLevel NOTICE \
    --RuleInfo.RuleInfoList.0.Status True \
    --RuleInfo.RuleInfoList.0.IsDelete False \
    --RuleInfo.RuleType USER_DEFINED_RULE \
    --RuleInfo.EffectAllCluster True \
    --RuleInfo.RuleID rule-id \
    --CopySrcRuleID src-rule-id \
    --EventID 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4a0dd046-0be4-434b-b212-f1a96636cc09",
        "RuleID": "d1b9dbe2-f78d-491a-b514-f0aa19d8ae4b"
    }
}
```

