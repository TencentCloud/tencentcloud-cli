**Example 1: 根据安全规则ID查询安全规则详情列表**



Input: 

```
tccli gaap DescribeSecurityRules --cli-unfold-argument  \
    --SecurityRuleIds sr-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "6dc6b074-9bcf-4120-9500-0583aebe375d",
        "SecurityRuleSet": [
            {
                "Protocol": "TCP",
                "SourceCidr": "1.1.1.101",
                "RuleId": "sr-0vr5571x",
                "DestPortRange": "6666,6667",
                "AliasName": "",
                "PolicyId": "sp-8k1l0pat",
                "Action": "ACCEPT"
            }
        ]
    }
}
```

