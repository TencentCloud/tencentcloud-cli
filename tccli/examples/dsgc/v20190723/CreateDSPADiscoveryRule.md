**Example 1: 新增分类分级规则**



Input: 

```
tccli dsgc CreateDSPADiscoveryRule --cli-unfold-argument  \
    --DspaId dspa-8zcer23c \
    --Name 账户余额 \
    --Description 账户余额 \
    --RDBRules.Status 0 \
    --RDBRules.MatchOperator or \
    --RDBRules.MetaRule.Operator and \
    --RDBRules.MetaRule.Contents.0.RuleType keyword \
    --RDBRules.MetaRule.Contents.0.RuleContent 账户|Account \
    --RDBRules.MetaRule.Contents.0.ExtendParameters.0.Name IsFullWordMatch \
    --RDBRules.MetaRule.Contents.0.ExtendParameters.0.Value false \
    --RDBRules.MetaRule.Contents.0.ExtendParameters.1.Name IsIgnoreCase \
    --RDBRules.MetaRule.Contents.0.ExtendParameters.1.Value true \
    --RDBRules.MetaRule.Contents.1.RuleType keyword \
    --RDBRules.MetaRule.Contents.1.RuleContent 余额|Balance \
    --RDBRules.MetaRule.Contents.1.ExtendParameters.0.Name IsFullWordMatch \
    --RDBRules.MetaRule.Contents.1.ExtendParameters.0.Value false \
    --RDBRules.MetaRule.Contents.1.ExtendParameters.1.Name IsIgnoreCase \
    --RDBRules.MetaRule.Contents.1.ExtendParameters.1.Value true \
    --RDBRules.ContentRule.Operator or \
    --RDBRules.ContentRule.Contents.0.RuleType regex \
    --RDBRules.ContentRule.Contents.0.RuleContent ^(((¥|\$)?(0|([1-9][0-9]*(,\d{3})*)|(([0]|([1-9][0-9]*(,\d{3})*))\.\d{1,2}))(yuan|.?元)?)|(人民币)?([圆角分零壹贰叁肆伍陆柒捌玖拾佰仟万亿]+[圆角分]))$ \
    --RDBRules.ContentRule.Contents.0.ExtendParameters None \
    --COSRules.RegexRule.Operator or \
    --COSRules.RegexRule.Contents.0.RuleContent (?<=\W)(((¥|\$)?(0|([1-9][0-9]*(,\d{3})*)|(([0]|([1-9][0-9]*(,\d{3})*))\.\d{1,2}))(yuan|.?元)?)|(人民币)?([圆角分零壹贰叁肆伍陆柒捌玖拾佰仟万亿]+[圆角分]))(?=\W) \
    --COSRules.RegexRule.Contents.0.IsIgnoreCase True \
    --COSRules.KeywordRule.Operator or \
    --COSRules.KeywordRule.Contents.0.RuleContent 账户余额 \
    --COSRules.KeywordRule.Contents.0.IsIgnoreCase True \
    --COSRules.KeywordRule.Contents.1.RuleContent Account Balance \
    --COSRules.KeywordRule.Contents.1.IsIgnoreCase True \
    --COSRules.KeywordRule.Contents.2.RuleContent AccountBalance \
    --COSRules.KeywordRule.Contents.2.IsIgnoreCase True \
    --COSRules.KeywordRule.Contents.3.RuleContent Account_Balance \
    --COSRules.KeywordRule.Contents.3.IsIgnoreCase True \
    --COSRules.IgnoreStringRule.Operator or \
    --COSRules.IgnoreStringRule.Contents None \
    --COSRules.MaxMatch 100 \
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

