**Example 1: 停用指定凭据**



Input: 

```
tccli ssm DisableSecret --cli-unfold-argument  \
    --SecretName lzctest
```

Output: 
```
{
    "Response": {
        "SecretName": "lzctest",
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

