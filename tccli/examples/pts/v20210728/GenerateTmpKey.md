**Example 1: 生成临时COS凭证**



Input: 

```
tccli pts GenerateTmpKey --cli-unfold-argument  \
    --ProjectId project-xx \
    --ScenarioId scenario-xx
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz",
        "StartTime": 1630376705,
        "ExpiredTime": 1630377005,
        "Credentials": {
            "TmpSecretId": "tmp-secretid-value",
            "TmpSecretKey": "tmp-secretkey-value",
            "Token": "token-value"
        }
    }
}
```

