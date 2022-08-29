**Example 1: demo**



Input: 

```
tccli vpc UpdateVmToUSGInternal --cli-unfold-argument  \
    --BindVMToUSGRequest.0.UsgIds sg-5q4brrm1 \
    --BindVMToUSGRequest.0.Uuid 84f9a2ad-6659-4864-808c-bd17f3c2acea \
    --BindVMToUSGRequest.0.SgId 251197522
```

Output: 
```
{
    "Response": {
        "BindVMToUSGResult": [
            {
                "Uuid": "84f9a2ad-6659-4864-808c-bd17f3c2acea",
                "ErrorCode": 511,
                "ErrorInfo": "No Record"
            }
        ],
        "ReturnCode": 504,
        "RequestId": "b3a7f48c-dbdf-429e-b4c1-ca616463c97c"
    }
}
```

