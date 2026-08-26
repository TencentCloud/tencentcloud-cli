**Example 1: 创建 ACL 规则示例**



Input: 

```
tccli csip CreateSandboxACLRule --cli-unfold-argument  \
    --RuleName 禁止出站访问未知域名 \
    --Level HIGH \
    --BelongAssetType HOST \
    --SystemRuleIDList 1001 \
    --EffectScope.EffectType EXCLUDE \
    --RuleAction BLOCK \
    --Status ON
```

Output: 
```
{
    "Response": {
        "ID": 2001,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

