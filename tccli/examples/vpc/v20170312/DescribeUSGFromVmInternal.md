**Example 1: demo**



Input: 

```
tccli vpc DescribeUSGFromVmInternal --cli-unfold-argument  \
    --GetUSGFromVMRequest.0.Uuid 84f9a2ad-6659-4864-808c-bd17f3c2acea
```

Output: 
```
{
    "Response": {
        "USGFromVMInfoSet": [
            {
                "Uuid": "84f9a2ad-6659-4864-808c-bd17f3c2acea",
                "UsgInfo": []
            }
        ],
        "ReturnCode": 0,
        "RequestId": "c31a7b90-b380-43b7-884c-56100c6c3310"
    }
}
```

