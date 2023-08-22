**Example 1: 删除防火墙模板规则**

删除防火墙模板规则

Input: 

```
tccli lighthouse DeleteFirewallTemplateRules --cli-unfold-argument  \
    --TemplateId lhft-6brh0ciy \
    --TemplateRuleIds lhftr-baaj68clja lhftr-bz6qfqut0i
```

Output: 
```
{
    "Response": {
        "RequestId": "215bc0ee-0700-4eab-b5ee-270c212e8deb"
    }
}
```

