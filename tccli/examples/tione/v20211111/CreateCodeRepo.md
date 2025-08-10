**Example 1: 创建代码仓库**



Input: 

```
tccli tione CreateCodeRepo --cli-unfold-argument  \
    --GitConfig.RepositoryUrl abc \
    --GitConfig.Branch master \
    --GitSecret.Secret test \
    --GitSecret.NoSecret True \
    --Name test
```

Output: 
```
{
    "Response": {
        "Id": "nb-123",
        "RequestId": "test123"
    }
}
```

