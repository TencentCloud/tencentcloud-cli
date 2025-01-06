**Example 1: 删除指定镜像**



Input: 

```
tccli tcr DeleteImage --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName multi-arch \
    --RepositoryName alpine \
    --ImageVersion 1
```

Output: 
```
{
    "Response": {
        "RequestId": "feeb9395-1fd7-41b4-8d1d-e791ca1cad5d"
    }
}
```

