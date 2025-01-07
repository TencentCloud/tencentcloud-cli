**Example 1: 创建个人版镜像仓库**



Input: 

```
tccli tcr CreateRepositoryPersonal --cli-unfold-argument  \
    --RepoName nicokang/golang1 \
    --Public 1 \
    --Description desc
```

Output: 
```
{
    "Response": {
        "RequestId": "190752c5-f87e-423f-93e4-eb426d82177d"
    }
}
```

