**Example 1: 验证COS分类分级规则**



Input: 

```
tccli dsgc VerifyDSPACOSRule --cli-unfold-argument  \
    --DspaId dspa-a1b2c3 \
    --Data keyword \
    --COSRules.Status 0 \
    --COSRules.RegexRule.Operator and \
    --COSRules.RegexRule.Contents.0.IsIgnoreCase True \
    --COSRules.RegexRule.Contents.0.RuleContent ^[1-9]$ \
    --COSRules.KeywordRule.Operator and \
    --COSRules.KeywordRule.Contents.0.IsIgnoreCase True \
    --COSRules.KeywordRule.Contents.0.RuleContent key \
    --COSRules.MaxMatch 0 \
    --COSRules.IgnoreStringRule.Operator and \
    --COSRules.IgnoreStringRule.Contents.0.IsIgnoreCase True \
    --COSRules.IgnoreStringRule.Contents.0.RuleContent good
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "VerifyResult": "Success",
        "DetailInfo": "验证成功"
    }
}
```

