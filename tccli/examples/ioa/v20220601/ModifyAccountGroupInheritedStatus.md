**Example 1: 修改分组继承的资源**

修改分组继承的资源

Input: 

```
tccli ioa ModifyAccountGroupInheritedStatus --cli-unfold-argument  \
    --Data.0.ResourceType 1 \
    --Data.0.ResourceId 1 \
    --Data.0.IsInherited True \
    --Data.0.AccountGroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

