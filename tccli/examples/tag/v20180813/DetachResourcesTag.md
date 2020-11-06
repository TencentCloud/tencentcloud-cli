**Example 1: Unbinding tag from multiple CVM instances in Guangzhou**



Input: 

```
tccli tag DetachResourcesTag --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourceRegion ap-guangzhou \
    --TagKey t1 \
    --TagValue v1 \
    --ResourcePrefix instance \
    --ResourceIds ins-001 ins-002
```

Output: 
```
{
    "Response": {
        "RequestId": "7bf7fd57-4d48-4a5a-957a-80b390dea667"
    }
}
```

