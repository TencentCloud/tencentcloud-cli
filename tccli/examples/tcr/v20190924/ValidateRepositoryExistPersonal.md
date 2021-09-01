**Example 1: 验证个人版仓库是否存在**



Input: 

```
tccli tcr ValidateRepositoryExistPersonal --cli-unfold-argument  \
    --RepoName dockerhub/test
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsExist": false
        },
        "RequestId": "444332c8-056a-4f8a-899b-16ba6e2d0be5"
    }
}
```

