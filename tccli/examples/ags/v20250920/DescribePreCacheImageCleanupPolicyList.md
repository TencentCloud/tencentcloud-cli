**Example 1: 按ID查询镜像预热清理策略**



Input: 

```
tccli ags DescribePreCacheImageCleanupPolicyList --cli-unfold-argument  \
    --CleanupPolicyIds pccp-peuhhczu
```

Output: 
```
{
    "Response": {
        "CleanupPolicySet": [
            {
                "CleanupPolicyId": "pccp-peuhhczu",
                "CreateTime": "2026-11-17T08:27:41Z",
                "Enabled": true,
                "IdleTTL": "1d",
                "Name": "example2",
                "RegistryHost": "tcr-cq.tencentcloudcr.com",
                "RepoPattern": "test/*",
                "UpdateTime": "2026-11-17T08:28:13Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "84861c4e-e29f-443b-a952-0120053f31e6"
    }
}
```

