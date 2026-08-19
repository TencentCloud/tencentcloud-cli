**Example 1: 查询指定lighthouse实例对应的防火墙规则**



Input: 

```
tccli csip DescribeLighthouseFirewallRules --cli-unfold-argument  \
    --AssetID lhins-j**u9*xp \
    --MemberId mem-68b80*7a6*2**000
```

Output: 
```
{
    "Response": {
        "FirewallRules": [
            {
                "Action": "ACCEPT",
                "AppType": "自定义",
                "CidrBlock": "10.1.1.32",
                "FirewallRuleDescription": "32",
                "Ipv6CidrBlock": "",
                "Port": "32",
                "Protocol": "TCP"
            }
        ],
        "RequestId": "735398a5-0084-4470-b000-62d6a9bae635"
    }
}
```

