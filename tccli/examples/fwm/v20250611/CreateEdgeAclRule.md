**Example 1: 创建互联网边界规则**



Input: 

```
tccli fwm CreateEdgeAclRule --cli-unfold-argument  \
    --GroupId fwmrg-a47wwiregj \
    --Rules.0.OrderIndex 1 \
    --Rules.0.Direction 1 \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.TargetContent 0.0.0.0/0 \
    --Rules.0.TargetType net \
    --Rules.0.Port -1/-1 \
    --Rules.0.Protocol TCP \
    --Rules.0.RuleAction accept \
    --Rules.0.Description 21212 \
    --Rules.0.Scope all
```

Output: 
```
{
    "Response": {
        "RuleIds": [
            "74ae6caf-979c-4528-8187-a389533e6fd8"
        ],
        "RequestId": "385384d2-7ece-4151-9aa6-66f8df839614"
    }
}
```

