**Example 1: 删除个人版镜像仓库Tag自动清理策略**



Input: 

```
tccli tcr DeleteImageLifecyclePersonal --cli-unfold-argument  \
    --RepoName dockerhub/test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

