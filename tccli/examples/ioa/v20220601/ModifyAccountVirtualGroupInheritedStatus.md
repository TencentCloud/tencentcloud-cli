**Example 1: 取消用户继承的自定义分组资源**

取消用户继承的自定义分组资源

Input: 

```
tccli ioa ModifyAccountVirtualGroupInheritedStatus --cli-unfold-argument  \
    --Data.0.ResourceType 1 \
    --Data.0.ResourceId 1 \
    --Data.0.IsInherited True \
    --Data.0.AccountId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

