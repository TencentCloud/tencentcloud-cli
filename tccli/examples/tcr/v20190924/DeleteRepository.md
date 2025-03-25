**Example 1: 删除镜像仓库**

删除镜像仓库以及仓库内的镜像列表

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

