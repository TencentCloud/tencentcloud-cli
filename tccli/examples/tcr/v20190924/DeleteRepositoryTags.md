**Example 1: 批量删除镜像仓库Tag**



Input: 

```
tccli tcr DeleteRepositoryTags --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --NamespaceName test \
    --RepositoryName demo \
    --Tags tag0
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

