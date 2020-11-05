**Example 1: Disabling a Secret**



Input: 

```
tccli ssm DisableSecret --cli-unfold-argument  \
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

