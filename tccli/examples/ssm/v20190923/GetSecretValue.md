**Example 1: Obtaining the plaintext of a Secret**



Input: 

```
tccli ssm GetSecretValue --cli-unfold-argument  \
    --SecretName test_secret \
    --VersionId v1.0
```

Output: 
```
{
    "Response": {
        "RequestId": "b8e6b67f-3ca7-4341-b4fa-a372bdf4e11c",
        "SecretName": "test_secret",
        "VersionId": "v1.0",
        "SecretBinary": "",
        "SecretString": "test"
    }
}
```

