**Example 1: 批量删除镜像仓库Tag**



Input: 

```
tccli tcr DeleteRepositoryTags --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName public \
    --RepositoryName golang \
    --Tags 1 2
```

Output: 
```
{
    "Response": {
        "RequestId": "6f337112-efb5-4b49-9430-bb980089f4ea"
    }
}
```

