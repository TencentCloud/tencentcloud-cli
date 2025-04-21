**Example 1: 删除用户授权业务资源**

删除用户授权业务资源

Input: 

```
tccli ioa DeleteAccountResources --cli-unfold-argument  \
    --ResourceList.0.ResourceType 2 \
    --ResourceList.0.ResourceId 3684 \
    --AccountId 927122
```

Output: 
```
{
    "Response": {
        "RequestId": "54ffeb21-6c61-4161-9845-269f33b925d3"
    }
}
```

