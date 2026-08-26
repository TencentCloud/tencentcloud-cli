**Example 1: 调用示例**



Input: 

```
tccli csip ModifySandboxFileRule --cli-unfold-argument  \
    --MemberId mem-tencent-0************50 \
    --RuleID 43 \
    --RuleContent.RuleName modify-example \
    --RuleContent.BelongAssetType HOST \
    --RuleContent.EffectScope.EffectType EXCLUDE \
    --RuleContent.Action RO \
    --RuleContent.PathWhitelist /etc/ \
    --RuleContent.Status ON
```

Output: 
```
{
    "Response": {
        "RuleID": 43,
        "RequestId": "0683f7cc-4545-42a5-ac79-baaab13ce400"
    }
}
```

