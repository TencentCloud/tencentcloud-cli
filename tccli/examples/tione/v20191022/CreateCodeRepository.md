**Example 1: 创建无密钥的存储库**

创建一个基于Git协议的无密钥存储库

Input: 

```
tccli tione CreateCodeRepository --cli-unfold-argument  \
    --CodeRepositoryName public \
    --GitConfig.RepositoryUrl https://github.com/example/test.git \
    --GitConfig.Branch master \
    --GitSecret.NoSecret true
```

Output: 
```
{
    "Response": {
        "RequestId": "15837630207346314662",
        "CodeRepositoryName": "public"
    }
}
```

**Example 2: 创建有密钥的存储库**

创建一个基于Git协议的需要密钥的存储库

Input: 

```
tccli tione CreateCodeRepository --cli-unfold-argument  \
    --CodeRepositoryName private \
    --GitConfig.RepositoryUrl https://github.com/example/test.git \
    --GitConfig.Branch master \
    --GitSecret.Secret {"UserName":"xxx","Password":"xxx"}
```

Output: 
```
{
    "Response": {
        "RequestId": "15837630207346314662",
        "CodeRepositoryName": "private"
    }
}
```

