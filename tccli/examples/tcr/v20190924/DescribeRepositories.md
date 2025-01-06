**Example 1: 查询镜像仓库信息**

查询指定实例内全部镜像仓库

Input: 

```
tccli tcr DescribeRepositories --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName multi-arch \
    --RepositoryName busybox \
    --Offset 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RepositoryList": [
            {
                "BriefDescription": "busybox",
                "CreationTime": "2024-12-10 14:30:36.806284 +0000 UTC",
                "Description": "",
                "Name": "multi-arch/busybox",
                "Namespace": "multi-arch",
                "Public": false,
                "UpdateTime": "2024-12-10 14:30:36.806284 +0000 UTC"
            }
        ],
        "RequestId": "1cce5817-43d2-4f50-9fd5-e807d3ea0768",
        "TotalCount": 1
    }
}
```

