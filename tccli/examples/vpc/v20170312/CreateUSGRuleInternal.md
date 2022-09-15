**Example 1: USG插入规则**



Input: 

```
tccli vpc CreateUSGRuleInternal --cli-unfold-argument  \
    --InsertUSGRuleRequest.0.UsgId 123123 \
    --InsertUSGRuleRequest.0.Direction inbound \
    --InsertUSGRuleRequest.0.Version 12 \
    --InsertUSGRuleRequest.0.Policies.0.Protocol tcp \
    --InsertUSGRuleRequest.0.Policies.0.Ip 10.0.0.0/8 \
    --InsertUSGRuleRequest.0.Policies.0.Id sg-e5qrs5d9 \
    --InsertUSGRuleRequest.0.Policies.0.ServiceModule ppm-ni1v9ozg \
    --InsertUSGRuleRequest.0.Policies.0.AddressModule ipmg-liaueln6 \
    --InsertUSGRuleRequest.0.Policies.0.Action ACCEPT \
    --InsertUSGRuleRequest.0.Policies.0.Port 80 \
    --InsertUSGRuleRequest.0.Policies.0.Desc test \
    --InsertUSGRuleRequest.0.Index 1
```

Output: 
```
{
    "Response": {
        "InsertUSGRuleResult": [
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

