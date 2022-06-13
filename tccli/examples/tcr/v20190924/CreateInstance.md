**Example 1: 创建企业版实例**



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

**Example 2: test**



Input: 

```
tccli tcr CreateInstance --cli-unfold-argument  \
    --RegistryName dongjwwang-my-test \
    --RegistryType basic
```

Output: 
```
{
    "Response": {
        "RequestId": "947cec54-bafd-4da9-8e07-2ac22e8ed6d4",
        "RegistryId": "for-test"
    }
}
```

