**Example 1: 创建镜像仓库**



Input: 

```
tccli tcr CreateSignature --cli-unfold-argument  \
    --NamespaceName library \
    --RepositoryName nginx \
    --RegistryId tcr-okmju7 \
    --ImageVersion v1.2.0
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

