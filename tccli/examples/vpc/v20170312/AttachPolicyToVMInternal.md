**Example 1: CVM新增规则**



Input: 

```
tccli vpc AttachPolicyToVMInternal --cli-unfold-argument  \
    --AddPolicyToVMRequest.0.IsTop True \
    --AddPolicyToVMRequest.0.Uuid 84f9a2ad-6659-4864-808c-bd17f3c2acea \
    --AddPolicyToVMRequest.0.Policies.0.Action DROP \
    --AddPolicyToVMRequest.0.Policies.0.Ip 111.108.86.20 \
    --AddPolicyToVMRequest.0.Policies.0.Direction INPUT \
    --AddPolicyToVMRequest.0.Policies.0.Protocol TCP \
    --AddPolicyToVMRequest.0.Policies.0.Port 80
```

Output: 
```
{
    "Response": {
        "AddPolicyToVMResult": [
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

