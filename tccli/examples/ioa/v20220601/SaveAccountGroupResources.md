**Example 1: 添加资源授权**



Input: 

```
tccli ioa SaveAccountGroupResources --cli-unfold-argument  \
    --AccountGroupId 135030 \
    --ResourceList.0.ResourceId 15625 \
    --ResourceList.0.ResourceType 1 \
    --ResourceList.0.ExpireTime 0 \
    --ResourceList.1.ResourceId 15626 \
    --ResourceList.1.ResourceType 1 \
    --ResourceList.1.ExpireTime 0
```

Output: 
```
{
    "Response": {
        "RequestId": "2d149043-9997-4dfc-a103-444b2eb17a88"
    }
}
```

