**Example 1: 创建镜像预热清理策略**



Input: 

```
tccli ags CreatePreCacheImageCleanupPolicy --cli-unfold-argument  \
    --Name example \
    --IdleTTL 3d \
    --Enabled False \
    --RegistryHost tcr-cq.tencentcloudcr.com
```

Output: 
```
{
    "Response": {
        "CleanupPolicy": {
            "CleanupPolicyId": "pccp-fipjvbm0",
            "CreateTime": "2026-11-17T08:30:48Z",
            "Enabled": false,
            "IdleTTL": "3d",
            "Name": "example",
            "RegistryHost": "tcr-cq.tencentcloudcr.com",
            "RepoPattern": "",
            "UpdateTime": "2026-11-17T08:30:48Z"
        },
        "RequestId": "ba91d0c1-8b57-4c59-8775-c7ecbef99fab"
    }
}
```

