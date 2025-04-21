**Example 1: 为用户授权业务资源**

为用户授权业务资源

Input: 

```
tccli ioa SaveAccountResources --cli-unfold-argument  \
    --ResourceList.0.ResourceType 1 \
    --ResourceList.0.ResourceId 1 \
    --ResourceList.0.ExpireTime 1 \
    --AccountId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

