**Example 1: 删除防火墙规则**



Input: 

```
tccli lighthouse DeleteFirewallRules --cli-unfold-argument  \
    --InstanceId lhins-aglzynfg \
    --FirewallRules.0.Protocol TCP \
    --FirewallRules.0.Port 80 \
    --FirewallRules.1.Protocol UDP \
    --FirewallRules.1.Port 22,443 \
    --FirewallRules.2.Protocol TCP \
    --FirewallRules.2.Port 8000-8081
```

Output: 
```
{
    "Response": {
        "RequestId": "b5182261-ab41-4801-a702-be05f2277758"
    }
}
```

