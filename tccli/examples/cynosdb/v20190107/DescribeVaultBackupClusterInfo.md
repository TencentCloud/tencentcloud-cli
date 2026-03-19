**Example 1: 查询保险箱下备份所属集群信息**



Input: 

```
tccli cynosdb DescribeVaultBackupClusterInfo --cli-unfold-argument  \
    --VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a
```

Output: 
```
{
    "Response": {
        "ClusterInfos": [
            {
                "ClusterId": "cynosdbmysql-h30xf5d7",
                "ClusterName": "backupT_202602021412",
                "ClusterRegion": "ap-guangzhou",
                "ClusterStatus": "deleted",
                "ClusterZone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "34994a5c-df6c-4ff0-8de6-295665165d35"
    }
}
```

