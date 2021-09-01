**Example 1: 添加防火墙规则**



Input: 

```
tccli lighthouse CreateFirewallRules --cli-unfold-argument  \
    --InstanceId lhins-aglzynfg \
    --FirewallRules.0.Protocol TCP \
    --FirewallRules.0.Port 80 \
    --FirewallRules.1.Protocol UDP \
    --FirewallRules.1.Port 22,443 \
    --FirewallRules.2.Protocol TCP \
    --FirewallRules.2.Port 8000-8080
```

Output: 
```
{
    "Response": {
        "RequestId": "667cc0c1-fa3e-4752-a36b-4bf45ec4bc7d"
    }
}
```

