**Example 1: 个人版镜像仓库批量删除Tag**



Input: 

```
tccli tcr BatchDeleteImagePersonal --cli-unfold-argument  \
    --RepoName dockerhub/test \
    --Tags 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

