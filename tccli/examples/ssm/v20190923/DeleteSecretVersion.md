**Example 1: Deleting a Secret version**



Input: 

```
tccli ssm DeleteSecretVersion --cli-unfold-argument  \
    --SecretName test\
    --VersionId v1.0
```

Output: 
```
{
    "Response": {
        "RequestId": "c701cf6d-4199-4822-8630-d48ee953f485",
        "SecretName": "test",
        "VersionId": "v1.0"
    }
}
```

