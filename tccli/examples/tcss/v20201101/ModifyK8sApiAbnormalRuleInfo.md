**Example 1: 修改k8sapi异常规则信息**



Input: 

```
tccli tcss ModifyK8sApiAbnormalRuleInfo --cli-unfold-argument  \
    --RuleInfo.Status True \
    --RuleInfo.RuleInfoList.0.Action RULE_MODE_ALERT \
    --RuleInfo.RuleInfoList.0.IsDelete False \
    --RuleInfo.RuleInfoList.0.RiskLevel NOTICE \
    --RuleInfo.RuleInfoList.0.Scope {"RequestURI":"/apis/cowsajhhoa.k8s.io/v","RequestUser":"“name”:”sanpasahsad-contaosaer-leader”）\"","ResponseStatusCode":"200","SourceIPS":"10.255.0.43","UserAgent":"snapshot-controller","Verb":"update"} \
    --RuleInfo.RuleInfoList.0.Status True \
    --RuleInfo.RuleID d1b9dbe2-f78d-491a-b514-f0aa19d8ae4b \
    --RuleInfo.RuleType USER_DEFINED_RULE \
    --RuleInfo.EffectAllCluster True \
    --RuleInfo.RuleName rulename-test
```

Output: 
```
{
    "Response": {
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd"
    }
}
```

