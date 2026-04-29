**Example 1: 给资源授权某个分组**



Input: 

```
tccli ioa GrantResourcesByAccountGroups --cli-unfold-argument  \
    --Operations.0.OperationType 1 \
    --Operations.0.ResourceId 1 \
    --Operations.0.ResourceType 2 \
    --Operations.0.ExpireTime 1 \
    --Operations.0.AccountGroupId 2571
```

Output: 
```
{
    "Response": {
        "RequestId": "c392af65-c12c-4fd0-b97e-1138dffbbbfd"
    }
}
```

