**Example 1: 批量启用 DLP 规则示例**



Input: 

```
tccli csip ModifySandboxDLPRuleStatus --cli-unfold-argument  \
    --IDList 4001 4002 \
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

