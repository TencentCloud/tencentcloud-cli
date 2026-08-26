**Example 1: 创建 DLP 规则示例**



Input: 

```
tccli csip CreateSandboxDLPRule --cli-unfold-argument  \
    --RuleName 出境敏感数据防护 \
    --Level HIGH \
    --BelongAssetType CONTAINER \
    --UserRuleContent.0.RuleName 身份证号 \
    --UserRuleContent.0.RuleContent [1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[0-9Xx] \
    --EffectScope.EffectType EXCLUDE \
    --RuleAction BLOCK \
    --Status ON
```

Output: 
```
{
    "Response": {
        "ID": 4001,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

