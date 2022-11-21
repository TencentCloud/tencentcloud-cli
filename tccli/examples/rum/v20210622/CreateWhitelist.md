**Example 1: 创建白名单**



Input: 

```
tccli rum CreateWhitelist --cli-unfold-argument  \
    --InstanceID taw-123 \
    --Aid 222 \
    --Remark 备注 \
    --WhitelistUin 1123
```

Output: 
```
{
    "Response": {
        "Msg": "xx",
        "ID": 1,
        "RequestId": "xx"
    }
}
```

**Example 2: 12**



Input: 

```
tccli rum CreateWhitelist --cli-unfold-argument  \
    --InstanceID taw-123 \
    --Aid 333 \
    --Remark 222 \
    --WhitelistUin 22323
```

Output: 
```
{
    "Response": {
        "ID": 77,
        "Msg": "success",
        "RequestId": "fcaec326-8c68-4302-8624-c5b08b9f1893"
    }
}
```

