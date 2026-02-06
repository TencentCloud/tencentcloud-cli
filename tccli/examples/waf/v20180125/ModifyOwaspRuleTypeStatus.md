**Example 1: 修改类型开关**



Input: 

```
tccli waf ModifyOwaspRuleTypeStatus --cli-unfold-argument  \
    --Domain owasp.saas3.testwaf.com \
    --TypeIDs 10000000 \
    --RuleTypeStatus 0
```

Output: 
```
{
    "Response": {
        "RequestId": "7ef51e76-fc98-4281-86f9-69ef620494e0"
    }
}
```

