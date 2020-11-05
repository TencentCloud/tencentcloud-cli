**Example 1: Enabling a Secret**



Input: 

```
tccli ssm EnableSecret --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "SecretName": "test",
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

