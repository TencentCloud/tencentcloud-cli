**Example 1: OperateApplicationTcrBinding**



Input: 

```
tccli tsf OperateApplicationTcrBinding --cli-unfold-argument  \
    --TcrRepoInfo.RegistryName xx \
    --TcrRepoInfo.Namespace xx \
    --TcrRepoInfo.Region 1 \
    --TcrRepoInfo.RegistryId xx \
    --TcrRepoInfo.RepoName xx \
    --Command xx \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

