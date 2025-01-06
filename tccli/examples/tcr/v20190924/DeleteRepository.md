**Example 1: 删除镜像仓库**



Input: 

```
tccli tcr DeleteRepository --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName private \
    --RepositoryName golang
```

Output: 
```
{
    "Response": {
        "RequestId": "ca2eddea-14cc-4c3f-96e5-de50fd1fd4c0"
    }
}
```

