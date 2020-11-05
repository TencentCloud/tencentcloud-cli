**Example 1: Obtaining the list of versions of a Secret**



Input: 

```
tccli ssm ListSecretVersionIds --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "RequestId": "56fe436b-16ca-402e-a9bb-83c14e9cc9e8",
        "SecretName": "test",
        "Versions": [
            {
                "VersionId": "v2.0",
                "CreateTime": 1574161372
            },
            {
                "VersionId": "v1.0",
                "CreateTime": 1574161748
            }
        ]
    }
}
```

