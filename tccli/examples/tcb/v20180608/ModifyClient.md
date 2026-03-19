**Example 1: 修改客户端配置**

修改AccessToken和RefreshToken失效时间以及最大在线会话数

Input: 

```
tccli tcb ModifyClient --cli-unfold-argument  \
    --EnvId env-123 \
    --Id env-123 \
    --RefreshTokenExpiresIn 2592000 \
    --MaxDevice 3 \
    --AccessTokenExpiresIn 7200
```

Output: 
```
{
    "Response": {
        "RequestId": "da6c7a9e-efa2-46c9-b13d-f02cc2ceafda"
    }
}
```

