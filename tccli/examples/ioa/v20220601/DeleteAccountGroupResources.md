**Example 1: 取消用户组资源授权**

取消用户组的业务资源授权

Input: 

```
tccli ioa DeleteAccountGroupResources --cli-unfold-argument  \
    --ResourceList.0.ResourceType 2 \
    --ResourceList.0.ResourceId 3684 \
    --AccountGroupId 189477
```

Output: 
```
{
    "Response": {
        "RequestId": "491edf66-4522-462a-b6d7-5d4653a81360"
    }
}
```

