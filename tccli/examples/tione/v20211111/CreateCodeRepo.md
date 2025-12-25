**Example 1: 创建代码仓库**



Input: 

```
tccli tione CreateCodeRepo --cli-unfold-argument  \
    --GitConfig.RepositoryUrl  \
    --GitConfig.Branch master \
    --GitSecret.Secret  \
    --GitSecret.NoSecret True \
    --Name 
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

