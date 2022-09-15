**Example 1: 设置CVM隔离级别**



Input: 

```
tccli vpc ModifyVmIsolationInternal --cli-unfold-argument  \
    --IsolateVMRequest.0.Uuid ssssss \
    --IsolateVMRequest.0.IsolateLevel 0
```

Output: 
```
{
    "Response": {
        "IsolateVMResult": [
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

