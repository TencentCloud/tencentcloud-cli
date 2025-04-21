**Example 1: 修改自定义用户组**

修改自定义用户组

Input: 

```
tccli ioa ModifyAccountVirtualGroup --cli-unfold-argument  \
    --VirtualGroupId 12 \
    --VirtualGroupName 虚拟组1 \
    --Description 描述
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

