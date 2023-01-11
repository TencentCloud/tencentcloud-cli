**Example 1: 创建企业版实例**

创建实例

Input: 

```
tccli tcr CreateInstance --cli-unfold-argument  \
    --RegistryName tcr-test \
    --RegistryType standard \
    --SyncTag True
```

Output: 
```
{
    "Response": {
        "RegistryId": "XXXX",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

