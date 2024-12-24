**Example 1: 修改分类分级规则**



Input: 

```
tccli dsgc ModifyDSPADiscoveryRule --cli-unfold-argument  \
    --DspaId dspa-a2cb7812 \
    --Name 手机号 \
    --RuleId 0 \
    --Description 用户的手机号 \
    --RDBRules.Status 0 \
    --RDBRules.MatchOperator or \
    --RDBRules.MetaRule.Operator or \
    --RDBRules.MetaRule.Contents.0.RuleType regex \
    --RDBRules.MetaRule.Contents.0.RuleContent 一个正则表达式字符串 \
    --RDBRules.ContentRule.Operator or \
    --RDBRules.ContentRule.Contents.0.RuleType keyword \
    --RDBRules.ContentRule.Contents.0.RuleContent 某关键词 \
    --COSRules.Status 0 \
    --COSRules.RegexRule.Operator and \
    --COSRules.RegexRule.Contents.0.RuleContent 一个正则表达式字符串 \
    --COSRules.RegexRule.Contents.0.IsIgnoreCase True \
    --COSRules.KeywordRule.Operator or \
    --COSRules.KeywordRule.Contents.0.RuleContent 某关键词 \
    --COSRules.KeywordRule.Contents.0.IsIgnoreCase True \
    --COSRules.IgnoreStringRule.Operator or \
    --COSRules.MaxMatch 0 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

