**Example 1: 替换防火墙模板规则**

替换防火墙模板规则

Input: 

```
tccli lighthouse ReplaceFirewallTemplateRule --cli-unfold-argument  \
    --TemplateId lhft-6brh0ciy \
    --TemplateRuleId lhftr-baaj68clja \
    --TemplateRule.Protocol UDP \
    --TemplateRule.Port 811 \
    --TemplateRule.CidrBlock 0.0.0.0/0 \
    --TemplateRule.Action DROP \
    --TemplateRule.FirewallRuleDescription udp 80
```

Output: 
```
{
    "Response": {
        "RequestId": "49d3c62e-9daa-4db5-b8f3-2498bb1dde36"
    }
}
```

