**Example 1: 添加IPV6转换规则**

添加IPV6转换规则。

Input: 

```
tccli vpc AddIp6Rules --cli-unfold-argument  \
    --Ip6TranslatorId ip6-90pt7p9q \
    --Ip6RuleInfos.0.Vport6 55 \
    --Ip6RuleInfos.0.Vip 106.54.197.66 \
    --Ip6RuleInfos.0.Protocol TCP \
    --Ip6RuleInfos.0.Vport 66
```

Output: 
```
{
    "Response": {
        "Ip6RuleSet": [
            "rule6-f3se1mki"
        ],
        "RequestId": "fd8c7584-b5e7-4d93-99bd-470ed0aa51e7"
    }
}
```

