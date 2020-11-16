**Example 1: 解绑多个广州地域的云主机实例关联的某个标签**



Input: 

```
tccli tag DetachResourcesTag --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourceRegion ap-guangzhou \
    --TagKey t1 \
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

