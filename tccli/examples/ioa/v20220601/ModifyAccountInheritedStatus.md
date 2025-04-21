**Example 1: 修改用户继承资源状态**

修改用户继承资源状态

Input: 

```
tccli ioa ModifyAccountInheritedStatus --cli-unfold-argument  \
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

