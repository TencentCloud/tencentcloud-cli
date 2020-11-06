**Example 1: 删除指定镜像**



Input: 

```
tccli tcr DeleteImage --cli-unfold-argument  \
    --RegistryId tcr-okmj78 \
    --NamespaceName mytest \
    --RepositoryName test \
    --ImageVersion 1.0
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

