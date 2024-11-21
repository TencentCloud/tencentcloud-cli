**Example 1: 启用凭据**



Input: 

```
tccli ssm EnableSecret --cli-unfold-argument  \
    --SecretName test3-secret
```

Output: 
```
{
    "Response": {
        "SecretName": "test3-secret",
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

