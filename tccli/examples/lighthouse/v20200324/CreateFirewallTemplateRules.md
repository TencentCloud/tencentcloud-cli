**Example 1: 创建防火墙模板规则**

创建防火墙模板规则

Input: 

```
tccli lighthouse CreateFirewallTemplateRules --cli-unfold-argument  \
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
        "RequestId": "740970ad-8118-4cc7-bf35-5ca5352a682f",
        "TemplateRuleIdSet": [
            "lhftr-hmp4bn7q2o",
            "lhftr-b9evg1gakk"
        ]
    }
}
```

