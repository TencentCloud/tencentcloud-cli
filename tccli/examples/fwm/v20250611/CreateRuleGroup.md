**Example 1: 创建互联网边界防火墙规则组**



Input: 

```
tccli fwm CreateRuleGroup --cli-unfold-argument  \
    --GroupName cecece \
    --Product cfw_edge_acl
```

Output: 
```
{
    "Response": {
        "GroupId": "fwmrg-gdhhiywh3w",
        "RequestId": "71876973-7fd8-46be-9ffd-cde34473acbc"
    }
}
```

