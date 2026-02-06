**Example 1: 修改类型防护模式**



Input: 

```
tccli waf ModifyOwaspRuleTypeAction --cli-unfold-argument  \
    --Domain owasp.saas3.testwaf.com \
    --TypeIDs 10000000 \
    --RuleTypeAction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b034d2ed-102c-4266-aa74-113c8e2db3fb"
    }
}
```

