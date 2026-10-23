**Example 1: 用户更新密钥对**



Input: 

```
tccli tcb UpdateUserKey --cli-unfold-argument  \
    --Name 创建密钥对 \
    --KeyID adsrte-af342rfasdf \
    --AuthTypeCode code_template \
    --EnvId af13qfas-rasdfasdf \
    --Ext 
```

Output: 
```
{
    "Response": {
        "RequestId": "3b8b63a8-1b70-11f0-9cf9-fa6cef78999d",
        "UpdateResult": 1
    }
}
```

