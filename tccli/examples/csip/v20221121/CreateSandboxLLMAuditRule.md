**Example 1: 创建 LLM 审计规则示例**



Input: 

```
tccli csip CreateSandboxLLMAuditRule --cli-unfold-argument  \
    --RuleName 敏感意图审计 \
    --Level HIGH \
    --BelongAssetType HOST \
    --SystemRuleIDList grl-safety-politics-std grl-safety-prompt-001 \
    --EffectScope.EffectType EXCLUDE \
    --RuleAction BLOCK \
    --Status ON
```

Output: 
```
{
    "Response": {
        "ID": 6001,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

