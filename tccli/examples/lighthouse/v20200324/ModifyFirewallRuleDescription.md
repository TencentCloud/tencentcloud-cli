**Example 1: 修改防火墙规则描述**



Input: 

```
tccli lighthouse ModifyFirewallRuleDescription --cli-unfold-argument  \
    --InstanceId lhins-aglzynfg \
    --FirewallRule.Protocol TCP \
    --FirewallRule.Port 80 \
    --FirewallRule.FirewallRuleDescription 'test'
```

Output: 
```
{
    "Response": {
        "RequestId": "f9c1597d-90ef-4493-b6b4-bbc55f194a76"
    }
}
```

