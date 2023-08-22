**Example 1: 创建防火墙模板**

创建防火墙模板及规则

Input: 

```
tccli lighthouse CreateFirewallTemplate --cli-unfold-argument  \
    --TemplateName test-create \
    --TemplateRules.0.Protocol TCP \
    --TemplateRules.0.Port 80 \
    --TemplateRules.0.CidrBlock 0.0.0.0/0 \
    --TemplateRules.0.Action ACCEPT \
    --TemplateRules.0.FirewallRuleDescription tcp 80 \
    --TemplateRules.1.Protocol UDP \
    --TemplateRules.1.Port 80 \
    --TemplateRules.1.CidrBlock 0.0.0.0/0 \
    --TemplateRules.1.Action DROP \
    --TemplateRules.1.FirewallRuleDescription udp 80
```

Output: 
```
{
    "Response": {
        "RequestId": "aa00f8e0-fe60-4902-bee6-5c6162fbd429",
        "TemplateId": "lhft-6brh0ciy"
    }
}
```

