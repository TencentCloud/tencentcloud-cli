**Example 1: 信息防泄漏切换规则开关**



Input: 

```
tccli waf ModifyAntiInfoLeakRuleStatus --cli-unfold-argument  \
    --Domain www.test.com \
    --RuleId 123 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "800f0a0c-6f8b-409a-af67-ccd12354e8f4"
    }
}
```

