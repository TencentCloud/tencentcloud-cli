**Example 1: 调用示例**



Input: 

```
tccli csip CreateSandboxFileRule --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29 \
    --RuleContent.RuleName allow dot local bin \
    --RuleContent.BelongAssetType HOST \
    --RuleContent.EffectScope.EffectType EXCLUDE \
    --RuleContent.Action RO \
    --RuleContent.PathWhitelist /home/dev/.local/bin \
    --RuleContent.Status ON
```

Output: 
```
{
    "Response": {
        "RuleID": 2,
        "RequestId": "56fc76be-fbee-4b60-987f-d557be45db33"
    }
}
```

