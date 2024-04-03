**Example 1: 重置服务级账号密码**

重置服务级账号密码

Input: 

```
tccli tcr ModifyServiceAccountPassword --cli-unfold-argument  \
    --RegistryId tcr-gijwqid7 \
    --Name robot \
    --Random True
```

Output: 
```
{
    "Response": {
        "Password": "kukui1ECDL8kr9cm6W66Me8PlhHemFmC",
        "RequestId": "60e7d0ce-c8ed-4495-9814-9397482f0d4a"
    }
}
```

**Example 2: 自定义服务级账号密码**

自定义服务级账号密码

Input: 

```
tccli tcr ModifyServiceAccountPassword --cli-unfold-argument  \
    --RegistryId tcr-gijwqid7 \
    --Name robot \
    --Random False \
    --Password NewPass123
```

Output: 
```
{
    "Response": {
        "Password": "NewPass123",
        "RequestId": "8c63b1e6-02b8-48af-94c2-416aa71e0c12"
    }
}
```

