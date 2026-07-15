**Example 1: 查询规则详情（规则组管理）**



Input: 

```
tccli fwm DescribeSecurityGroupRule --cli-unfold-argument  \
    --RuleId b36302b0-3a24-43d7-8d5a-2e24d6e68c89 \
    --GroupId fwmrg-6wq0b6j0
```

Output: 
```
{
    "Response": {
        "RequestId": "812242b4-c71a-4a14-a907-1f36e440c53e",
        "Rule": {
            "Detail": "1",
            "DstContent": "::/0",
            "DstPort": "-1/-1",
            "DstType": "net",
            "IpVersion": "ipv6",
            "Protocol": "ANY",
            "ProtocolPortType": 1,
            "Region": "",
            "RuleAction": "accept",
            "RuleId": "b36302b0-3a24-43d7-8d5a-2e24d6e68c89",
            "Scope": "SG",
            "Sequence": 1,
            "ServiceTemplateId": "ppm-r7gw5s50",
            "SrcContent": "2402:4e00:c032:8800:be66:c9b8:2454:0",
            "SrcType": "net"
        }
    }
}
```

