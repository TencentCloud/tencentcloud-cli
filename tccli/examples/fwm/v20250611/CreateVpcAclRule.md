**Example 1: 添加VPC 规则**



Input: 

```
tccli fwm CreateVpcAclRule --cli-unfold-argument  \
    --GroupId fwmrg-1j95tza8s6 \
    --Rules.0.SourceContent 0.0.0.0/0 \
    --Rules.0.SourceType net \
    --Rules.0.DestContent 0.0.0.0/0 \
    --Rules.0.DestType net \
    --Rules.0.Protocol ANY \
    --Rules.0.RuleAction accept \
    --Rules.0.OrderIndex 1 \
    --Rules.0.EdgeId all \
    --Rules.0.FwGroupId ALL \
    --Rules.0.Port -1/-1 \
    --Rules.0.Description 3232
```

Output: 
```
{
    "Response": {
        "RuleIds": [
            "4bf3f7c5-9b0b-45c6-ae6e-3641848a93a1"
        ],
        "RequestId": "0cbb5305-41e5-4367-b8d2-d930a457ae8b"
    }
}
```

