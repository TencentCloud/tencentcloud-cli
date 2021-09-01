**Example 1: 更新个人版镜像仓库描述**



Input: 

```
tccli tcr ModifyRepositoryInfoPersonal --cli-unfold-argument  \
    --RepoName dockerhub/test \
    --Description mytest
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

