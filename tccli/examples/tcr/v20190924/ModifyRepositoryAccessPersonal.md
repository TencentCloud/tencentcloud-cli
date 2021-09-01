**Example 1: 更新个人版仓库访问属性**



Input: 

```
tccli tcr ModifyRepositoryAccessPersonal --cli-unfold-argument  \
    --RepoName dockerhub/test \
    --Public 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

