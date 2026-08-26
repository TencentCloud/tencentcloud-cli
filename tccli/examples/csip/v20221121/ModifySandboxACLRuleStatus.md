**Example 1: 批量启用 ACL 规则示例**



Input: 

```
tccli csip ModifySandboxACLRuleStatus --cli-unfold-argument  \
    --IDList 2001 2002 \
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

