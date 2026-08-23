**Example 1: 批量启用 LLM 审计规则示例**



Input: 

```
tccli csip ModifySandboxLLMAuditRuleStatus --cli-unfold-argument  \
    --IDList 6001 6002 \
    --Status ON
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

