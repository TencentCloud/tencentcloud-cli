**Example 1: 验证COS分类分级规则**



Input: 

```
tccli dsgc VerifyDSPACOSRule --cli-unfold-argument  \
    --DspaId xx \
    --Data xx \
    --COSRules.Status 0 \
    --COSRules.RegexRule.Operator xx \
    --COSRules.RegexRule.Contents.0.IsIgnoreCase True \
    --COSRules.RegexRule.Contents.0.RuleContent xx \
    --COSRules.KeywordRule.Operator xx \
    --COSRules.KeywordRule.Contents.0.IsIgnoreCase True \
    --COSRules.KeywordRule.Contents.0.RuleContent xx \
    --COSRules.MaxMatch 0 \
    --COSRules.IgnoreStringRule.Operator xx \
    --COSRules.IgnoreStringRule.Contents.0.IsIgnoreCase True \
    --COSRules.IgnoreStringRule.Contents.0.RuleContent xx
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "VerifyResult": "Success",
        "DetailInfo": ""
    }
}
```

