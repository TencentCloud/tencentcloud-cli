**Example 1: 新增分类分级规则**



Input: 

```
tccli dsgc CreateDSPADiscoveryRule --cli-unfold-argument  \
    --DspaId abc \
    --Name abc \
    --Description abc \
    --RDBRules.Status 0 \
    --RDBRules.MatchOperator abc \
    --RDBRules.MetaRule.Operator abc \
    --RDBRules.MetaRule.Contents.0.RuleType abc \
    --RDBRules.MetaRule.Contents.0.RuleContent abc \
    --RDBRules.MetaRule.Contents.0.ExtendParameters.0.Name abc \
    --RDBRules.MetaRule.Contents.0.ExtendParameters.0.Value abc \
    --RDBRules.ContentRule.Operator abc \
    --RDBRules.ContentRule.Contents.0.RuleType abc \
    --RDBRules.ContentRule.Contents.0.RuleContent abc \
    --RDBRules.ContentRule.Contents.0.ExtendParameters.0.Name abc \
    --RDBRules.ContentRule.Contents.0.ExtendParameters.0.Value abc \
    --COSRules.Status 0 \
    --COSRules.RegexRule.Operator abc \
    --COSRules.RegexRule.Contents.0.RuleContent abc \
    --COSRules.RegexRule.Contents.0.IsIgnoreCase True \
    --COSRules.KeywordRule.Operator abc \
    --COSRules.KeywordRule.Contents.0.RuleContent abc \
    --COSRules.KeywordRule.Contents.0.IsIgnoreCase True \
    --COSRules.IgnoreStringRule.Operator abc \
    --COSRules.IgnoreStringRule.Contents.0.RuleContent abc \
    --COSRules.IgnoreStringRule.Contents.0.IsIgnoreCase True \
    --COSRules.MaxMatch 0 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "RuleId": 1
    }
}
```

