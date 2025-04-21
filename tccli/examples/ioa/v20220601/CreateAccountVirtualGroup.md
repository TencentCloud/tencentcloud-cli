**Example 1: 创建自定义用户组**

创建自定义用户组

Input: 

```
tccli ioa CreateAccountVirtualGroup --cli-unfold-argument  \
    --VirtualGroupName 自定义用户组1 \
    --Description 描述 \
    --AccountGroupId 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "VirtualGroupId": 123
        },
        "RequestId": "abc"
    }
}
```

