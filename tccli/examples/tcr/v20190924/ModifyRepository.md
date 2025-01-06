**Example 1: 更新镜像仓库信息**



Input: 

```
tccli tcr ModifyRepository --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName ns1 \
    --RepositoryName golang \
    --BriefDescription golang \
    --Description golang
```

Output: 
```
{
    "Response": {
        "RequestId": "488d0f66-ef02-4efc-a5e5-be8c9b39203e"
    }
}
```

