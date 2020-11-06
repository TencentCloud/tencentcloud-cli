**Example 1: 更新存储库秘钥**



Input: 

```
tccli tione UpdateCodeRepository --cli-unfold-argument  \
    --CodeRepositoryName private \
    --GitSecret.Secret '{"UserName":"xxx", "Password":"xxx"}'
```

Output: 
```
{
    "Response": {
        "RequestId": "15837643767558277241",
        "CodeRepositoryName": "private"
    }
}
```

