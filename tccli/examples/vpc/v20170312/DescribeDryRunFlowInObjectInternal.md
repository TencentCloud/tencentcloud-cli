**Example 1: demo**



Input: 

```
tccli vpc DescribeDryRunFlowInObjectInternal --cli-unfold-argument  \
    --Direction inbound \
    --Objects 84f9a2ad-6659-4864-808c-bd17f3c2acea \
    --Flows.0.SrcIp 10.0.0.0 \
    --Flows.0.DstIp 10.0.10.0 \
    --Flows.0.DstPort 80 \
    --Flows.0.Protocol tcp \
    --ObjectType 0
```

Output: 
```
{
    "Response": {
        "DryRunFlowInObjectResult": [
            {
                "FlowIndex": "0",
                "ObjectCheckResult": [
                    {
                        "Object": "84f9a2ad-6659-4864-808c-bd17f3c2acea",
                        "CheckResult": "ACCEPT"
                    }
                ]
            }
        ],
        "ReturnCode": 0,
        "RequestId": "55061ba0-863f-4211-a5ed-dfba366c5f6f"
    }
}
```

