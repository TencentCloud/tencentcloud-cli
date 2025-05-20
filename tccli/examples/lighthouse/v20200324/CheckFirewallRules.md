**Example 1: 查询防火墙规则放通状态。**

查询防火墙规则放通状态。

Input: 

```
tccli lighthouse CheckFirewallRules --cli-unfold-argument  \
    --InstanceId lhins-aglzynfg \
    --FirewallRules.0.Protocol TCP \
    --FirewallRules.0.Port 8081 \
    --FirewallRules.1.Protocol UDP \
    --FirewallRules.1.Port 8082
```

Output: 
```
{
    "Response": {
        "ActiveFirewallRuleSet": [
            {
                "AppType": "自定义",
                "Protocol": "TCP",
                "Port": "8081",
                "CidrBlock": "0.0.0.0/0",
                "FirewallRuleDescription": "",
                "Action": "ACCEPT"
            }
        ],
        "InactiveFirewallRuleSet": [
            {
                "Protocol": "UDP",
                "Port": "8082",
                "FirewallRuleDescription": "",
                "CidrBlock": "0.0.0.0/0",
                "AppType": "自定义",
                "Action": "ACCEPT"
            }
        ],
        "RequestId": "667cc0c1-fa3e-4752-a36b-4bf45ec4bc7d"
    }
}
```

