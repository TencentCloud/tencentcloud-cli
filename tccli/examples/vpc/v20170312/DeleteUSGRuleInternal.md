**Example 1: USG删除规则**



Input: 

```
tccli vpc DeleteUSGRuleInternal --cli-unfold-argument  \
    --DeleteUSGRuleRequest.0.UsgId 123123 \
    --DeleteUSGRuleRequest.0.Direction inbound \
    --DeleteUSGRuleRequest.0.Version 12 \
    --DeleteUSGRuleRequest.0.Indexes 2 1
```

Output: 
```
{
    "Response": {
        "DeleteUSGRuleResult": [
            {
                "UsgId": "sg-dn7qcw21",
                "ErrorCode": 0,
                "ErrorInfo": "success"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

