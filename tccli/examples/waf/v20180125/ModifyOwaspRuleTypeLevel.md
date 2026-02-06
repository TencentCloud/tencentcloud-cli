**Example 1: 修改类型防护等级**



Input: 

```
tccli waf ModifyOwaspRuleTypeLevel --cli-unfold-argument  \
    --Domain owasp.saas3.testwaf.com \
    --TypeIDs 10000000 \
    --RuleTypeLevel 100
```

Output: 
```
{
    "Response": {
        "RequestId": "6a776d3a-5bbe-4ee4-a3bb-5a41ba18aa56"
    }
}
```

