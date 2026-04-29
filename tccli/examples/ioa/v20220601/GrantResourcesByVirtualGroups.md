**Example 1: 增加授权**



Input: 

```
tccli ioa GrantResourcesByVirtualGroups --cli-unfold-argument  \
    --Operations.0.OperationType 1 \
    --Operations.0.ResourceId 7 \
    --Operations.0.ResourceType 1 \
    --Operations.0.ExpireTime 0 \
    --Operations.0.VirtualAccountGroupId 544
```

Output: 
```
{
    "Response": {
        "RequestId": "16979b9c-08f5-48bf-95e5-ac143dacb3ae"
    }
}
```

