**Example 1: 获取临时实例访问凭证**

获取实例的临时访问凭证，有效期仅 1 小时，可用于临时登录。

Input: 

```
tccli tcr CreateInstanceToken --cli-unfold-argument  \
    --RegistryId tcr-ak9876 \
    --TokenType temp
```

Output: 
```
{
    "Response": {
        "Username": 12345678,
        "Token": "XXXX",
        "ExpTime": "33987631",
        "RequestId": "xx",
        "TokenId": "xx"
    }
}
```

**Example 2: 获取长期实例访问凭证**

获取实例的长期有效的访问凭证，可用于第三方应用授权。

Input: 

```
tccli tcr CreateInstanceToken --cli-unfold-argument  \
    --RegistryId tcr-ak9876 \
    --TokenType longterm \
    --Desc for-tke-cluster
```

Output: 
```
{
    "Response": {
        "Username": 12345678,
        "Token": "XXXX",
        "ExpTime": "33987631",
        "RequestId": "xx",
        "TokenId": "1456976"
    }
}
```

