**Example 1: OperateApplicationTcrBinding**



Input: 

```
tccli tsf OperateApplicationTcrBinding --cli-unfold-argument  \
    --TcrRepoInfo.RegistryName register-name \
    --TcrRepoInfo.Namespace tsf_127273497 \
    --TcrRepoInfo.Region 1 \
    --TcrRepoInfo.RegistryId ngxin \
    --TcrRepoInfo.RepoName ngxin \
    --Command bind \
    --ApplicationId application-6a79x94v
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

