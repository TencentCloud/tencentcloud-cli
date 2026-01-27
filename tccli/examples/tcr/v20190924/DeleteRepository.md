**Example 1: 删除不存在镜像的镜像仓库**

当镜像仓库不存在镜像时，删除镜像仓库

Input: 

```
tccli tcr DeleteRepository --cli-unfold-argument  \
    --RegistryId tcr-40s86s0j \
    --NamespaceName dev \
    --RepositoryName nginx \
    --ForceDelete False
```

Output: 
```
{
    "Response": {
        "RequestId": "b04639d7-cd4e-4ea7-b0b8-cf962fdcfcbe"
    }
}
```

**Example 2: 删除镜像仓库**

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

**Example 3: 删除镜像仓库调用失败**

删除存在镜像的仓库时，参数ForceDelete=false，删除失败

Input: 

```
tccli tcr DeleteRepository --cli-unfold-argument  \
    --RegistryId tcr-dc0dgswk \
    --NamespaceName dev \
    --RepositoryName nginx \
    --ForceDelete False
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.PreconditionFailed",
            "Message": "repository is not empty, cannot delete without ForceDelete=true"
        },
        "RequestId": "824a3cdf-f20d-44bd-ac63-d132d64e0c9c"
    }
}
```

