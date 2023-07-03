**Example 1: 修改防火墙规则**

修改防火墙规则

Input: 

```
tccli lighthouse ModifyFirewallRules --cli-unfold-argument  \
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
        "RequestId": "f927b1f4-5734-4ada-ab76-6b2bb0614c6d"
    }
}
```

