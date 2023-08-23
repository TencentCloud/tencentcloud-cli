**Example 1: 重置防火墙模版下所有规则**

重置防火墙模版下所有规则

Input: 

```
tccli lighthouse ResetFirewallTemplateRules --cli-unfold-argument  \
    --TemplateId lhft-6brh0ciy \
    --TemplateRules.0.Protocol TCP \
    --TemplateRules.0.Port 81 \
    --TemplateRules.0.CidrBlock 0.0.0.0/0 \
    --TemplateRules.0.Action ACCEPT \
    --TemplateRules.0.FirewallRuleDescription tcp 80 \
    --TemplateRules.1.Protocol UDP \
    --TemplateRules.1.Port 81 \
    --TemplateRules.1.CidrBlock 0.0.0.0/0 \
    --TemplateRules.1.Action DROP \
    --TemplateRules.1.FirewallRuleDescription udp 80
```

Output: 
```
{
    "Response": {
        "RequestId": "1bf93010-2454-434a-915d-be102f47700c",
        "TemplateRuleIdSet": [
            "lhftr-gexf7cmvpq",
            "lhftr-9uxz9zuz62"
        ]
    }
}
```

