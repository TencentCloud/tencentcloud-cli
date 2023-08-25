**Example 1: 修改分类分级规则**



Input: 

```
tccli dsgc ModifyDSPADiscoveryRule --cli-unfold-argument  \
    --DspaId xx \
    --Name xx \
    --RuleId 123 \
    --RDBRules.Status 0 \
    --RDBRules.MatchOperator xx \
    --RDBRules.MetaRule.Operator xx \
    --RDBRules.MetaRule.Contents.0.RuleType xx \
    --RDBRules.MetaRule.Contents.0.RuleContent xx \
    --RDBRules.ContentRule.Operator xx \
    --RDBRules.ContentRule.Contents.0.RuleType xx \
    --RDBRules.ContentRule.Contents.0.RuleContent xx \
    --COSRules.Status 0 \
    --COSRules.RegexRule.Operator or \
    --COSRules.RegexRule.Contents.0.RuleContent xx \
    --COSRules.KeywordRule.Operator xx \
    --COSRules.KeywordRule.Contents.0.IsIgnoreCase False \
    --COSRules.KeywordRule.Contents.0.RuleContent xx \
    --COSRules.MaxMatch 0 \
    --COSRules.IgnoreStringRule.Operator xx \
    --COSRules.IgnoreStringRule.Contents.0.IsIgnoreCase False \
    --COSRules.IgnoreStringRule.Contents.0.RuleContent xx \
    --Description xx
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

