**Example 1: 更新镜像仓库信息**



Input: 

```
tccli tcr ModifyRepository --cli-unfold-argument  \
    --RegistryId tcr-okmj78 \
    --NamespaceName mytest \
    --RepositoryName test \
    --Description mytest \
    --BriefDescription BriefDescription
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

