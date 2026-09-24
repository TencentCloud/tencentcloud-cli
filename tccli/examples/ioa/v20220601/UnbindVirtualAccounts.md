**Example 1: 从自定义用户组移除用户**

从自定义用户组移除用户

Input: 

```
tccli ioa UnbindVirtualAccounts --cli-unfold-argument  \
    --VirtualGroupId 12 \
    --AccountIdList 12
```

Output: 
```
{
    "Response": {
        "RequestId": "1bc"
    }
}
```

