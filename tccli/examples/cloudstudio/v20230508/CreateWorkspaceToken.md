**Example 1: 为工作空间创建临时访问凭证**

为工作空间创建临时访问凭证，重复调用会创建新的 Token，旧的 Token 将会自动失效

Input: 

```
tccli cloudstudio CreateWorkspaceToken --cli-unfold-argument  \
    --SpaceKey bpwsmb \
    --TokenExpiredLimitSec 3600 \
    --Policies workspace-run-only
```

Output: 
```
{
    "Response": {
        "Token": "83c99d6a03aa94f5e7bbfb4eded0de0b1153f44d05126d34b5f36e8343eca973",
        "ExpiredTime": "2023-02-13T12:33:48 GMT+08:00",
        "RequestId": "6e1e1482-cfe6-4462-a508-4fc7053a0c78"
    }
}
```

