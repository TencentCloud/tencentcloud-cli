**Example 1: 给广州地域多个云主机实例关联标签**



Input: 

```
tccli tag AttachResourcesTag --cli-unfold-argument  \
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
        "RequestId": "7bf7fd57-4d48-4a5a-957a-80b390dea117"
    }
}
```

