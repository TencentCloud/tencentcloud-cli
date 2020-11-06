**Example 1: 删除镜像仓库**



Input: 

```
tccli tcr DeleteRepository --cli-unfold-argument  \
    --RegistryId tcr-okmj78 \
    --NamespaceName test \
    --RepositoryName mytest
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

