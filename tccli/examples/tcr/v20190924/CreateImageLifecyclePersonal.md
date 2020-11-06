**Example 1: 设置个人版仓库tag清理策略**



Input: 

```
tccli tcr CreateImageLifecyclePersonal --cli-unfold-argument  \
    --RepoName dockerhub/test \
    --Type keep_last_days \
    --Val 5
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

