**Example 1: CVM删除规则**



Input: 

```
tccli vpc DeletePolicyFromVmInternal --cli-unfold-argument  \
    --DeletePolicyFromVmRequest.0.Uuid 123123 \
    --DeletePolicyFromVmRequest.0.Policies.0.Action ACCEPT \
    --DeletePolicyFromVmRequest.0.Policies.0.Ip 10.0.0.0/8 \
    --DeletePolicyFromVmRequest.0.Policies.0.Direction INPUT \
    --DeletePolicyFromVmRequest.0.Policies.0.Protocol tcp \
    --DeletePolicyFromVmRequest.0.Policies.0.Port 80
```

Output: 
```
{
    "Response": {
        "DeletePolicyFromVmResult": [
            {
                "Uuid": "84f9a2ad-6659-4864-808c-bd17f3c2acea",
                "ErrorCode": 0,
                "ErrorInfo": "success"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

