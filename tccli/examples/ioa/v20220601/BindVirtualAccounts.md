**Example 1: 向自定义用户组添加用户**

向自定义用户组添加用户

Input: 

```
tccli ioa BindVirtualAccounts --cli-unfold-argument  \
    --VirtualGroupId 12 \
    --AccountIdList 12
```

Output: 
```
{
    "Response": {
        "RequestId": "adc"
    }
}
```

