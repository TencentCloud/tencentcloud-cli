**Example 1: 验证分类分级规则**



Input: 

```
tccli dsgc VerifyDSPADiscoveryRule --cli-unfold-argument  \
    --VerifyContent keyword \
    --DspaId dspa-001 \
    --MetaRule.Operator and \
    --MetaRule.Contents.0.RuleType keyword \
    --MetaRule.Contents.0.RuleContent number \
    --ContentRule.Operator and \
    --ContentRule.Contents.0.RuleType keyword \
    --ContentRule.Contents.0.RuleContent success \
    --VerifyMeta keyword \
    --MatchOperator and
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

