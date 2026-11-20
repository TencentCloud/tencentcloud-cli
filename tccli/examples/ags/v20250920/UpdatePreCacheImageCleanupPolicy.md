**Example 1: 更新镜像预热自动清理策略**



Input: 

```
tccli ags UpdatePreCacheImageCleanupPolicy --cli-unfold-argument  \
    --CleanupPolicyId pccp-fipjvbm0 \
    --RegistryHost tcr-cq.tencentcloudcr.com \
    --RepoPattern example/* \
    --Enabled False
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
            "RepoPattern": "example/*",
            "UpdateTime": "2026-11-17T08:36:20Z"
        },
        "RequestId": "71677a5f-4661-4b84-a30d-00b705f52aba"
    }
}
```

