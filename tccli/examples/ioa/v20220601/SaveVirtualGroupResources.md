**Example 1: 为自定义用户组授权业务资源**

为自定义用户组授权业务资源

Input: 

```
tccli ioa SaveVirtualGroupResources --cli-unfold-argument  \
    --ResourceList.0.ResourceType 1 \
    --ResourceList.0.ResourceId 1 \
    --ResourceList.0.ExpireTime 1 \
    --VirtualGroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

